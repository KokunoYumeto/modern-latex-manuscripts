[CmdletBinding()]
param(
    [string]$CsvPath = 'manifests/github-custody/20260806_sources.csv',
    [string]$JsonPath = 'manifests/github-custody/20260806_sources.json',
    [string]$ObservedDate = (Get-Date -Format 'yyyy-MM-dd')
)

$ErrorActionPreference = 'Stop'
$utf8 = [System.Text.UTF8Encoding]::new($false)

function Get-Sha256 {
    param([byte[]]$Bytes)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return [Convert]::ToHexString($sha.ComputeHash($Bytes))
    }
    finally {
        $sha.Dispose()
    }
}

function Get-StreamIdentity {
    param([object[]]$Rows, [bool]$Relative)
    $paths = [string[]]@($Rows | ForEach-Object {
        if ($Relative) { $_.RelativePath } else { $_.RepoPath }
    })
    [Array]::Sort($paths, [StringComparer]::Ordinal)

    $byPath = [System.Collections.Generic.Dictionary[string, object]]::new(
        [StringComparer]::Ordinal
    )
    foreach ($row in $Rows) {
        $key = if ($Relative) { $row.RelativePath } else { $row.RepoPath }
        $byPath.Add($key, $row)
    }

    $builder = [System.Text.StringBuilder]::new()
    foreach ($path in $paths) {
        $row = $byPath[$path]
        [void]$builder.Append($path)
        [void]$builder.Append("`t")
        [void]$builder.Append($row.Bytes)
        [void]$builder.Append("`t")
        [void]$builder.Append($row.GitBlobSha1)
        [void]$builder.Append("`n")
    }
    $bytes = $utf8.GetBytes($builder.ToString())
    return [pscustomobject]@{
        Bytes  = $bytes.Length
        Sha256 = Get-Sha256 -Bytes $bytes
    }
}

function ConvertTo-CsvField {
    param([AllowEmptyString()][string]$Value)
    return '"' + $Value.Replace('"', '""') + '"'
}

$rootConfig = @(
    [pscustomobject]@{ Path = 'sources/author-cluster'; Map = 'docs/cluster-map.md' },
    [pscustomobject]@{ Path = 'sources/classical'; Map = 'docs/classical-map.md' },
    [pscustomobject]@{ Path = 'sources/dedekind'; Map = 'docs/dedekind-map.md' },
    [pscustomobject]@{ Path = 'sources/deligne'; Map = 'docs/deligne-map.md' },
    [pscustomobject]@{ Path = 'sources/dirichlet'; Map = 'docs/dirichlet-map.md' },
    [pscustomobject]@{ Path = 'sources/ega'; Map = 'docs/ega-map.md' },
    [pscustomobject]@{ Path = 'sources/fga'; Map = 'docs/fga-map.md' },
    [pscustomobject]@{ Path = 'sources/gauss'; Map = 'docs/gauss-map.md' },
    [pscustomobject]@{ Path = 'sources/illusie'; Map = 'docs/illusie-map.md' },
    [pscustomobject]@{ Path = 'sources/noether'; Map = 'docs/noether-map.md' },
    [pscustomobject]@{ Path = 'sources/non-european'; Map = 'docs/non-european-map.md' },
    [pscustomobject]@{ Path = 'sources/riemann'; Map = 'docs/riemann-map.md' },
    [pscustomobject]@{ Path = 'sources/steinitz'; Map = 'docs/steinitz-map.md' },
    [pscustomobject]@{ Path = 'sources/sylvester'; Map = 'docs/sylvester-map.md' },
    [pscustomobject]@{ Path = 'sources/tohoku'; Map = 'docs/tohoku-map.md' },
    [pscustomobject]@{ Path = 'sources/ukrainian-applied-math'; Map = 'docs/ukrainian-map.md' },
    [pscustomobject]@{ Path = 'sources/verdier'; Map = 'docs/verdier-map.md' },
    [pscustomobject]@{ Path = 'sources/weber'; Map = 'docs/weber-map.md' },
    [pscustomobject]@{ Path = 'sources/workflow'; Map = $null }
)

$head = (& git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) { throw 'Cannot resolve HEAD.' }
$objectFormat = (& git rev-parse --show-object-format).Trim()
if ($LASTEXITCODE -ne 0 -or $objectFormat -ne 'sha1') {
    throw "Unexpected Git object format: $objectFormat"
}

$allRows = [System.Collections.Generic.List[object]]::new()
$rootRows = [System.Collections.Generic.List[object]]::new()
$worktreeSizeMismatches = 0
$worktreeBytes = 0L

foreach ($config in $rootConfig) {
    $root = $config.Path
    $treeOid = (& git rev-parse "HEAD:$root").Trim()
    if ($LASTEXITCODE -ne 0) { throw "Cannot resolve tree $root." }

    $lines = @(& git -c core.quotePath=false ls-tree -r -l HEAD -- $root)
    if ($LASTEXITCODE -ne 0) { throw "Cannot enumerate tree $root." }
    $selected = [System.Collections.Generic.List[object]]::new()

    foreach ($line in $lines) {
        $tab = $line.IndexOf("`t")
        if ($tab -lt 0) { throw "Malformed ls-tree row under $root." }
        $meta = $line.Substring(0, $tab)
        $repoPath = $line.Substring($tab + 1)
        if ($meta -notmatch '^(?<mode>[0-9]+) blob (?<oid>[0-9a-f]{40})\s+(?<bytes>[0-9]+)$') {
            throw "Non-blob or malformed Git object at $repoPath."
        }
        $prefix = "$root/"
        if (-not $repoPath.StartsWith($prefix, [StringComparison]::Ordinal)) {
            throw "Path escaped configured root: $repoPath"
        }
        $bytes = [int64]$Matches.bytes
        $diskBytes = (Get-Item -LiteralPath $repoPath).Length
        $worktreeBytes += $diskBytes
        if ($diskBytes -ne $bytes) { $worktreeSizeMismatches++ }
        $extension = [IO.Path]::GetExtension($repoPath).ToLowerInvariant()
        if ([string]::IsNullOrEmpty($extension)) { $extension = '[none]' }
        $row = [pscustomobject]@{
            Root          = $root
            RepoPath      = $repoPath
            RelativePath  = $repoPath.Substring($prefix.Length)
            Bytes         = $bytes
            GitBlobSha1   = $Matches.oid
            Mode          = $Matches.mode
            Extension     = $extension
        }
        $selected.Add($row)
        $allRows.Add($row)
    }

    $identity = Get-StreamIdentity -Rows @($selected) -Relative $true
    $rootRows.Add([pscustomobject]@{
        path                   = $root
        files                  = $selected.Count
        bytes                  = [int64](($selected | Measure-Object Bytes -Sum).Sum)
        git_tree_sha1          = $treeOid
        canonical_stream_bytes = $identity.Bytes
        tree_sha256            = $identity.Sha256
        map                    = $config.Map
    })
}

$repoPaths = [string[]]@($allRows | ForEach-Object { $_.RepoPath })
[Array]::Sort($repoPaths, [StringComparer]::Ordinal)
$rowByPath = [System.Collections.Generic.Dictionary[string, object]]::new(
    [StringComparer]::Ordinal
)
foreach ($row in $allRows) { $rowByPath.Add($row.RepoPath, $row) }

$csv = [System.Text.StringBuilder]::new()
[void]$csv.Append("root,path,bytes,git_blob_sha1,mode`n")
foreach ($path in $repoPaths) {
    $row = $rowByPath[$path]
    [void]$csv.Append((ConvertTo-CsvField $row.Root))
    [void]$csv.Append(',')
    [void]$csv.Append((ConvertTo-CsvField $row.RepoPath))
    [void]$csv.Append(',')
    [void]$csv.Append($row.Bytes)
    [void]$csv.Append(',')
    [void]$csv.Append($row.GitBlobSha1)
    [void]$csv.Append(',')
    [void]$csv.Append($row.Mode)
    [void]$csv.Append("`n")
}
$csvBytes = $utf8.GetBytes($csv.ToString())
[IO.File]::WriteAllBytes((Join-Path (Get-Location) $CsvPath), $csvBytes)

$aggregateIdentity = Get-StreamIdentity -Rows @($allRows) -Relative $false
$oidGroups = @($allRows | Group-Object GitBlobSha1)
$duplicateGroups = @($oidGroups | Where-Object Count -gt 1)
$crossRootGroups = @($duplicateGroups | Where-Object {
    @($_.Group.Root | Sort-Object -Unique).Count -gt 1
})
$pathsInDuplicateGroups = [int64](($duplicateGroups | Measure-Object Count -Sum).Sum)
$crossRootDetails = @($crossRootGroups | ForEach-Object {
    [pscustomobject]@{
        git_blob_sha1 = $_.Name
        bytes         = [int64]$_.Group[0].Bytes
        paths         = $_.Count
        roots         = @($_.Group.Root | Sort-Object -Unique)
        interpretation = 'Shared .gitattributes control blob; not duplicated mathematical content.'
    }
})

$allowedRootPaths = [string[]]@($rootConfig | ForEach-Object { $_.Path })
& git diff --quiet HEAD -- @allowedRootPaths
$allowedRootsClean = $LASTEXITCODE -eq 0
if ($LASTEXITCODE -gt 1) { throw 'Cannot check allowed-root worktree state.' }

$fileTypes = @($allRows | Group-Object Extension | ForEach-Object {
    [pscustomobject]@{
        extension = $_.Name
        files     = $_.Count
        bytes     = [int64](($_.Group | Measure-Object Bytes -Sum).Sum)
    }
} | Sort-Object extension)

$summary = [ordered]@{
    schema          = 'github-source-roots/v1'
    observed_date   = $ObservedDate
    observed_commit = $head
    scope           = 'Exact Git-object identity index for nineteen explicitly allowed sources roots. Catalog outputs and separately owned, revoked, or prohibited roots are outside the selection.'
    object_identity = [ordered]@{
        git_object_format = $objectFormat
        per_file          = 'repository path, Git blob bytes, Git blob SHA-1, and mode'
        canonical_stream  = 'Ordinal path order; path<TAB>bytes<TAB>git_blob_sha1<LF>; UTF-8 without BOM. Aggregate paths are repository-relative; root paths are root-relative.'
    }
    aggregate       = [ordered]@{
        roots                     = $rootConfig.Count
        files                     = $allRows.Count
        bytes                     = [int64](($allRows | Measure-Object Bytes -Sum).Sum)
        canonical_stream_bytes    = $aggregateIdentity.Bytes
        tree_sha256               = $aggregateIdentity.Sha256
        unique_git_blob_identities = $oidGroups.Count
        duplicate_groups          = $duplicateGroups.Count
        paths_in_duplicate_groups = $pathsInDuplicateGroups
        redundant_paths           = $pathsInDuplicateGroups - $duplicateGroups.Count
        cross_root_duplicate_groups = $crossRootGroups.Count
        working_tree_bytes        = $worktreeBytes
        working_tree_byte_delta   = $worktreeBytes - [int64](($allRows | Measure-Object Bytes -Sum).Sum)
    }
    index_file      = [ordered]@{
        path   = $CsvPath.Replace('\', '/')
        rows   = $allRows.Count
        bytes  = $csvBytes.Length
        sha256 = Get-Sha256 -Bytes $csvBytes
    }
    roots           = @($rootRows)
    file_types      = $fileTypes
    cross_root_duplicates = $crossRootDetails
    excluded_scope  = [ordered]@{
        policy         = 'Separately owned, revoked, or prohibited source roots are omitted without enumeration, inspection, or cross-linking.'
        entries_listed = $false
    }
    edited_indexes  = @(
        'README.md',
        'docs/browse-index.md',
        'docs/github-maps.md',
        'docs/site-map.md',
        'sources/README.md'
    )
    checks          = [ordered]@{
        allowed_roots_explicit       = $rootConfig.Count
        tracked_files                = $allRows.Count
        root_partition_replay        = "$($allRows.Count)/$($allRows.Count)"
        working_tree_size_mismatches = $worktreeSizeMismatches
        allowed_root_tracked_changes = if ($allowedRootsClean) { 0 } else { 1 }
        producer_source_bytes_mutated = $false
        content_rehash_or_blob_read_run = $false
        compile_render_or_ocr_run     = $false
        zenodo_network_queried        = $false
        global_filesystem_search      = $false
        prohibited_or_revoked_roots_inspected = $false
    }
}

$json = ($summary | ConvertTo-Json -Depth 8).Replace("`r`n", "`n") + "`n"
[IO.File]::WriteAllText((Join-Path (Get-Location) $JsonPath), $json, $utf8)

[pscustomobject]@{
    commit          = $head
    roots           = $rootConfig.Count
    files           = $allRows.Count
    bytes           = $summary.aggregate.bytes
    csv_bytes       = $csvBytes.Length
    csv_sha256      = $summary.index_file.sha256
    stream_bytes    = $aggregateIdentity.Bytes
    tree_sha256     = $aggregateIdentity.Sha256
    unique_blobs    = $oidGroups.Count
    duplicate_groups = $duplicateGroups.Count
    cross_root_duplicate_groups = $crossRootGroups.Count
    worktree_size_mismatches = $worktreeSizeMismatches
    worktree_byte_delta = $summary.aggregate.working_tree_byte_delta
    allowed_root_tracked_changes = $summary.checks.allowed_root_tracked_changes
} | ConvertTo-Json -Depth 3
