[CmdletBinding()]
param(
    [string]$OutputPath = 'manifests/github-custody/20260806_noether_routes.json',
    [string]$ObservedDate = (Get-Date -Format 'yyyy-MM-dd')
)

$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false)
$repoRoot = [IO.Path]::GetFullPath((Get-Location).Path)
$documents = [string[]]@('docs/noether-map.md', 'sources/noether/README.md')

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

$treeLines = @(& git -c core.quotepath=false ls-tree -d HEAD:sources/noether)
if ($LASTEXITCODE -ne 0) { throw 'Cannot list top-level Noether trees.' }
$trees = [Collections.Generic.Dictionary[string, string]]::new([StringComparer]::Ordinal)
foreach ($line in $treeLines) {
    if ($line -notmatch '^040000 tree ([0-9a-f]{40})\t(.+)$') {
        throw "Malformed top-level tree row: $line"
    }
    $trees.Add($matches[2], $matches[1])
}

$fileCounts = [Collections.Generic.Dictionary[string, int]]::new([StringComparer]::Ordinal)
$byteCounts = [Collections.Generic.Dictionary[string, long]]::new([StringComparer]::Ordinal)
$rootFileCount = 0
$rootFileBytes = [long]0
foreach ($name in $trees.Keys) {
    $fileCounts[$name] = 0
    $byteCounts[$name] = 0
}
$fileLines = @(& git -c core.quotepath=false ls-tree -r -l HEAD:sources/noether)
if ($LASTEXITCODE -ne 0) { throw 'Cannot list Noether file identities.' }
foreach ($line in $fileLines) {
    if ($line -notmatch '^\d+ blob [0-9a-f]{40}\s+(\d+)\t(.+)$') {
        throw "Malformed file row: $line"
    }
    $relativePath = $matches[2]
    if (-not $relativePath.Contains('/')) {
        $rootFileCount++
        $rootFileBytes += [long]$matches[1]
        continue
    }
    $name = ($relativePath -split '/', 2)[0]
    if (-not $trees.ContainsKey($name)) { throw "File outside a top-level tree: $relativePath" }
    $fileCounts[$name]++
    $byteCounts[$name] += [long]$matches[1]
}

$routeDocuments = [Collections.Generic.Dictionary[string, Collections.Generic.HashSet[string]]]::new([StringComparer]::Ordinal)
foreach ($name in $trees.Keys) {
    $routeDocuments[$name] = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
}
$documentRows = [Collections.Generic.List[object]]::new()
foreach ($document in $documents) {
    $bytes = Get-GitBlobBytes -Path $document
    $text = $utf8.GetString($bytes)
    foreach ($rawTarget in (Get-MarkdownTargets -Text $text)) {
        $target = Get-Destination -RawTarget $rawTarget
        if ([string]::IsNullOrWhiteSpace($target) -or $target.StartsWith('#')) { continue }
        if ($target -match '^[A-Za-z][A-Za-z0-9+.-]*:') { continue }
        $pathPart = (($target -split '#', 2)[0] -split '\?', 2)[0]
        $pathPart = [Uri]::UnescapeDataString($pathPart)
        if ([string]::IsNullOrWhiteSpace($pathPart)) { continue }
        $base = [IO.Path]::GetDirectoryName((Join-Path $repoRoot $document))
        $fullTarget = if ($pathPart.StartsWith('/')) {
            [IO.Path]::GetFullPath((Join-Path $repoRoot $pathPart.TrimStart('/')))
        }
        else {
            [IO.Path]::GetFullPath((Join-Path $base $pathPart))
        }
        $repoTarget = [IO.Path]::GetRelativePath($repoRoot, $fullTarget).Replace('\', '/')
        if (-not $repoTarget.StartsWith('sources/noether/', [StringComparison]::Ordinal)) { continue }
        $relative = $repoTarget.Substring('sources/noether/'.Length)
        $name = ($relative -split '/', 2)[0]
        if ($routeDocuments.ContainsKey($name)) { [void]$routeDocuments[$name].Add($document) }
    }
    $documentRows.Add([pscustomobject]@{
        path = $document
        bytes = $bytes.Length
        sha256 = Get-Sha256 -Bytes $bytes
    })
}

$names = [string[]]@($trees.Keys)
[Array]::Sort($names, [StringComparer]::Ordinal)
$rows = [Collections.Generic.List[object]]::new()
$canonical = [Text.StringBuilder]::new()
$unrouted = [Collections.Generic.List[string]]::new()
foreach ($name in $names) {
    $routeDocs = [string[]]@($routeDocuments[$name])
    [Array]::Sort($routeDocs, [StringComparer]::Ordinal)
    $routed = $routeDocs.Count -gt 0
    if (-not $routed) { $unrouted.Add($name) }
    $path = "sources/noether/$name"
    $rows.Add([pscustomobject]@{
        path = $path
        tree_oid = $trees[$name]
        files = $fileCounts[$name]
        bytes = $byteCounts[$name]
        routed = $routed
        route_documents = @($routeDocs)
    })
    [void]$canonical.Append($path)
    [void]$canonical.Append("`t")
    [void]$canonical.Append($trees[$name])
    [void]$canonical.Append("`t")
    [void]$canonical.Append($fileCounts[$name])
    [void]$canonical.Append("`t")
    [void]$canonical.Append($byteCounts[$name])
    [void]$canonical.Append("`t")
    [void]$canonical.Append($routed.ToString().ToLowerInvariant())
    [void]$canonical.Append("`t")
    [void]$canonical.Append(($routeDocs -join '|'))
    [void]$canonical.Append("`n")
}
$canonicalBytes = $utf8.GetBytes($canonical.ToString())

$result = [ordered]@{
    schema = 'github-noether-routes/v1'
    observed_date = $ObservedDate
    observed_commit = (& git rev-parse HEAD).Trim()
    scope = 'All tracked top-level Git trees directly below sources/noether and their human Markdown routes from the Noether coverage map or source landing.'
    canonical_stream = 'Ordinal path order; path<TAB>tree_oid<TAB>files<TAB>bytes<TAB>routed<TAB>route_documents joined by |<LF>; UTF-8 without BOM.'
    aggregate = [ordered]@{
        top_level_trees = $rows.Count
        files = [long](($rows | Measure-Object files -Sum).Sum)
        bytes = [long](($rows | Measure-Object bytes -Sum).Sum)
        routed_trees = $rows.Count - $unrouted.Count
        unrouted_trees = $unrouted.Count
        root_files_outside_tree_scope = $rootFileCount
        root_file_bytes_outside_tree_scope = $rootFileBytes
        route_documents = $documents.Count
        canonical_stream_bytes = $canonicalBytes.Length
        tree_sha256 = Get-Sha256 -Bytes $canonicalBytes
    }
    route_documents = @($documentRows)
    trees = @($rows)
    unrouted = @($unrouted)
    checks = [ordered]@{
        git_tree_inventory_replayed = "$($rows.Count)/$($rows.Count)"
        all_top_level_trees_human_routed = $unrouted.Count -eq 0
        working_tree_content_read = $false
        external_network_queried = $false
        producer_files_mutated = $false
        compile_render_or_ocr_run = $false
        global_filesystem_search = $false
        prohibited_or_revoked_roots_inspected = $false
    }
}

$json = (($result | ConvertTo-Json -Depth 7).Replace("`r`n", "`n")) + "`n"
[IO.File]::WriteAllText((Join-Path $repoRoot $OutputPath), $json, $utf8)

if ($unrouted.Count -ne 0) {
    throw "Unrouted Noether top-level trees: $($unrouted -join ', ')"
}

[pscustomobject]@{
    top_level_trees = $rows.Count
    files = $result.aggregate.files
    bytes = $result.aggregate.bytes
    routed_trees = $result.aggregate.routed_trees
    unrouted_trees = $result.aggregate.unrouted_trees
    tree_sha256 = $result.aggregate.tree_sha256
} | ConvertTo-Json -Compress
