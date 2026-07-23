[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SourceRoot,

    [Parameter(Mandatory = $true)]
    [string]$PredecessorSourceZip,

    [Parameter(Mandatory = $true)]
    [string]$OutputRoot
)

$ErrorActionPreference = 'Stop'

function Get-Identity {
    param([Parameter(Mandatory = $true)][string]$Path)

    $item = Get-Item -LiteralPath $Path
    [pscustomobject]@{
        bytes = [int64]$item.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $item.FullName).Hash
    }
}

function Get-RelativePathUnix {
    param(
        [Parameter(Mandatory = $true)][string]$BasePath,
        [Parameter(Mandatory = $true)][string]$Path
    )

    ([System.IO.Path]::GetRelativePath($BasePath, $Path)).Replace('\', '/')
}

function Get-StreamSha256 {
    param([Parameter(Mandatory = $true)][System.IO.Stream]$Stream)

    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        ([BitConverter]::ToString($sha.ComputeHash($Stream))).Replace('-', '')
    }
    finally {
        $sha.Dispose()
    }
}

function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Text
    )

    [System.IO.File]::WriteAllText(
        $Path,
        $Text,
        [System.Text.UTF8Encoding]::new($false)
    )
}

function Assert-Identity {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][int64]$Bytes,
        [Parameter(Mandatory = $true)][string]$Sha256
    )

    $identity = Get-Identity -Path $Path
    if ($identity.bytes -ne $Bytes -or $identity.sha256 -ne $Sha256) {
        throw "Identity mismatch: $Path"
    }
}

function New-DeterministicZip {
    param(
        [Parameter(Mandatory = $true)][string]$Source,
        [Parameter(Mandatory = $true)][string]$ZipPath
    )

    $stream = [System.IO.File]::Open(
        $ZipPath,
        [System.IO.FileMode]::CreateNew,
        [System.IO.FileAccess]::ReadWrite,
        [System.IO.FileShare]::None
    )
    try {
        $archive = [System.IO.Compression.ZipArchive]::new(
            $stream,
            [System.IO.Compression.ZipArchiveMode]::Create,
            $false
        )
        try {
            Get-ChildItem -LiteralPath $Source -Recurse -File |
                Sort-Object {
                    Get-RelativePathUnix -BasePath $Source -Path $_.FullName
                } |
                ForEach-Object {
                    $entryName = Get-RelativePathUnix `
                        -BasePath $Source `
                        -Path $_.FullName
                    $entry = $archive.CreateEntry(
                        $entryName,
                        [System.IO.Compression.CompressionLevel]::Optimal
                    )
                    $entry.LastWriteTime = [DateTimeOffset]::new(
                        2026, 7, 23, 0, 0, 0, [TimeSpan]::Zero
                    )
                    $input = [System.IO.File]::OpenRead($_.FullName)
                    try {
                        $output = $entry.Open()
                        try {
                            $input.CopyTo($output)
                        }
                        finally {
                            $output.Dispose()
                        }
                    }
                    finally {
                        $input.Dispose()
                    }
                }
        }
        finally {
            $archive.Dispose()
        }
    }
    finally {
        $stream.Dispose()
    }
}

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$source = (Resolve-Path -LiteralPath $SourceRoot).Path
$predecessorZip = (Resolve-Path -LiteralPath $PredecessorSourceZip).Path
if (Test-Path -LiteralPath $OutputRoot) {
    throw "Output root already exists: $OutputRoot"
}
New-Item -ItemType Directory -Force -Path (
    Split-Path -Parent $OutputRoot
) | Out-Null
New-Item -ItemType Directory -Path $OutputRoot | Out-Null
$output = (Resolve-Path -LiteralPath $OutputRoot).Path

$sourceFiles = @(
    Get-ChildItem -LiteralPath $source -Recurse -File |
        Sort-Object FullName
)
$sourceBytes = [int64](
    $sourceFiles | Measure-Object -Property Length -Sum
).Sum
if ($sourceFiles.Count -ne 199 -or $sourceBytes -ne 6911184) {
    throw "Unexpected payload boundary: $($sourceFiles.Count) files / $sourceBytes bytes."
}

$manifestPath = Join-Path $source 'SHA256SUMS.csv'
Assert-Identity `
    -Path $manifestPath `
    -Bytes 29207 `
    -Sha256 '2F78F112B9F5A368725E56AD432B13EAE9B8EE08052AC3B699C0A22452EE6DC8'
$manifestRows = @(Import-Csv -LiteralPath $manifestPath)
if ($manifestRows.Count -ne 198) {
    throw "Expected 198 payload manifest rows, found $($manifestRows.Count)."
}

$sourceByPath = @{}
foreach ($file in $sourceFiles) {
    $relative = Get-RelativePathUnix -BasePath $source -Path $file.FullName
    $sourceByPath[$relative] = Get-Identity -Path $file.FullName
}
$expectedPaths = @(
    @($manifestRows.relative_path) + 'SHA256SUMS.csv' |
        Sort-Object
)
$actualPaths = @($sourceByPath.Keys | Sort-Object)
if (
    [string]::Join("`n", $expectedPaths) -cne
    [string]::Join("`n", $actualPaths)
) {
    throw 'Payload exact-set mismatch.'
}
foreach ($row in $manifestRows) {
    $identity = $sourceByPath[$row.relative_path]
    if (
        $null -eq $identity -or
        $identity.bytes -ne [int64]$row.bytes -or
        $identity.sha256 -ne $row.sha256
    ) {
        throw "Payload manifest mismatch: $($row.relative_path)"
    }
}

$validationPath = Join-Path $source 'validation\PUBLIC_PAYLOAD_VALIDATION.json'
Assert-Identity `
    -Path $validationPath `
    -Bytes 3769 `
    -Sha256 '64375C38F21E4F69D62623EE980C4BFFB8F9C95CDE48EEC9F43395C5BEE5DB17'
$validation = Get-Content -LiteralPath $validationPath -Raw |
    ConvertFrom-Json
if ($validation.status -ne 'PASS' -or @($validation.errors).Count -ne 0) {
    throw 'Payload validation is not PASS/errors[].'
}

$pdfSource = Join-Path $source (
    'build\SGA3_English_Through_Expose_IV_Public_Checkpoint_20260723.pdf'
)
$masterSource = Join-Path $source 'tex\SGA3_English_Loop1.tex'
Assert-Identity `
    -Path $pdfSource `
    -Bytes 2675562 `
    -Sha256 'B717DC08C2C77546638274C7F05266F5F24C1562999117ACF4D1874AFD79EA1D'
Assert-Identity `
    -Path $masterSource `
    -Bytes 8859 `
    -Sha256 'BD31E621C52AA7228BCD82A2AF827E68BB374DCF4473CBC4CF3E7E7D34E0CCE5'

$privacyPatterns = @(
    'C:\Users\Floris',
    'C:/Users/Floris',
    'C:\IL_GitHub',
    'Papors',
    'Chatnotes',
    'Claude',
    'Codex'
)
$textExtensions = @('.tex', '.md', '.csv', '.json', '.jsonl', '.txt', '.log')
foreach ($file in $sourceFiles) {
    if ($file.Extension.ToLowerInvariant() -notin $textExtensions) {
        continue
    }
    $text = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($pattern in $privacyPatterns) {
        if ($text -cmatch [regex]::Escape($pattern)) {
            throw "Privacy hit in payload: $($file.FullName) / $pattern"
        }
    }
}

# The source-derived images remain caveated, but this successor introduces no
# new image identity: every one is already present in the public predecessor.
$predecessorPngHashes = [System.Collections.Generic.HashSet[string]]::new(
    [System.StringComparer]::OrdinalIgnoreCase
)
$predecessorArchive = [System.IO.Compression.ZipFile]::OpenRead($predecessorZip)
try {
    foreach ($entry in $predecessorArchive.Entries) {
        if (
            [string]::IsNullOrEmpty($entry.Name) -or
            -not $entry.FullName.EndsWith(
                '.png',
                [StringComparison]::OrdinalIgnoreCase
            )
        ) {
            continue
        }
        $entryStream = $entry.Open()
        try {
            [void]$predecessorPngHashes.Add(
                (Get-StreamSha256 -Stream $entryStream)
            )
        }
        finally {
            $entryStream.Dispose()
        }
    }
}
finally {
    $predecessorArchive.Dispose()
}

$payloadPngs = @($sourceFiles | Where-Object { $_.Extension -eq '.png' })
if ($payloadPngs.Count -ne 128) {
    throw "Expected 128 payload PNGs, found $($payloadPngs.Count)."
}
foreach ($png in $payloadPngs) {
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $png.FullName).Hash
    if (-not $predecessorPngHashes.Contains($hash)) {
        throw "New source-pixel identity is not public in predecessor: $($png.FullName)"
    }
}

$pdfName = 'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf'
$masterName = (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex'
)
$zipName = (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_' +
    'Source_Ledgers_20260723.zip'
)
Copy-Item -LiteralPath $pdfSource -Destination (Join-Path $output $pdfName)
Copy-Item -LiteralPath $masterSource -Destination (Join-Path $output $masterName)
New-DeterministicZip `
    -Source $source `
    -ZipPath (Join-Path $output $zipName)

$archive = [System.IO.Compression.ZipFile]::OpenRead(
    (Join-Path $output $zipName)
)
try {
    $entries = @(
        $archive.Entries |
            Where-Object { -not [string]::IsNullOrEmpty($_.Name) }
    )
    if ($entries.Count -ne 199) {
        throw "Expected 199 ZIP members, found $($entries.Count)."
    }
    $zipUncompressedBytes = [int64](
        $entries | Measure-Object -Property Length -Sum
    ).Sum
    if ($zipUncompressedBytes -ne 6911184) {
        throw "Unexpected ZIP uncompressed bytes: $zipUncompressedBytes"
    }
    foreach ($entry in $entries) {
        if (
            $entry.FullName.StartsWith('/') -or
            $entry.FullName.StartsWith('\') -or
            $entry.FullName -match '^[A-Za-z]:' -or
            $entry.FullName -match '(^|/)\.\.(/|$)'
        ) {
            throw "Unsafe ZIP name: $($entry.FullName)"
        }
        $expected = $sourceByPath[$entry.FullName]
        if ($null -eq $expected -or $expected.bytes -ne $entry.Length) {
            throw "ZIP member path/byte mismatch: $($entry.FullName)"
        }
        $entryStream = $entry.Open()
        try {
            $actualHash = Get-StreamSha256 -Stream $entryStream
        }
        finally {
            $entryStream.Dispose()
        }
        if ($actualHash -ne $expected.sha256) {
            throw "ZIP member hash mismatch: $($entry.FullName)"
        }
    }
}
finally {
    $archive.Dispose()
}

$readme = @'
# SGA 3 English through Expose IV - public checkpoint r1

This compact archive package publishes the independently replayed English
working checkpoint through complete Expose IV.

- Reader: 266 A4 pages with deterministic creation metadata.
- Scope: Editorial Notice, Introduction, and complete Exposes I-IV.
- Expose IV diagrams: native TeX.
- Reference-v2 graph: 411 targets, 1,157 candidates/residuals, 611 linked
  edges, 1,519 PDF destinations, and 1,062 internal GoTo actions.
- Expose V remains a separate public working reader and is not superseded.
- Exposes VI-XXVI are not included.

The source ZIP contains all 199 exact files from the independently validated
public handoff: 56 editable TeX files, 128 required PNG assets, the reader,
machine ledgers, rights/provenance notes, and validation controls. Every PNG
is byte-identical to an asset already present in the predecessor public I-IV
archive, so this successor introduces no new source-pixel identity.

Rights in the underlying French work, Polo-Gille re-edition, and
source-derived diagram material remain with their holders. Jacob C.
Reinhold's `jcreinhold/sga` snapshot
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison lineage,
not authority. This is an incomplete scholarly working checkpoint, not a
critical edition, rights clearance, or complete SGA 3.
'@
Write-Utf8NoBom -Path (Join-Path $output 'README.md') -Text $readme

$outerRows = foreach ($name in @(
    'README.md',
    $pdfName,
    $masterName,
    $zipName
)) {
    $identity = Get-Identity -Path (Join-Path $output $name)
    [pscustomobject][ordered]@{
        relative_path = $name
        bytes = $identity.bytes
        sha256 = $identity.sha256
    }
}
$outerCsv = (($outerRows | ConvertTo-Csv -NoTypeInformation) -join "`r`n") +
    "`r`n"
Write-Utf8NoBom `
    -Path (Join-Path $output 'SHA256SUMS.csv') `
    -Text $outerCsv

$zipIdentity = Get-Identity -Path (Join-Path $output $zipName)
$packageBytesExcludingValidation = [int64](
    Get-ChildItem -LiteralPath $output -File |
        Measure-Object -Property Length -Sum
).Sum
$packageValidation = [ordered]@{
    status = 'PASS'
    errors = @()
    scope = 'SGA3 cumulative English working checkpoint through Expose IV'
    source_root_mutated = $false
    package_files = 6
    package_bytes_excluding_validation = $packageBytesExcludingValidation
    outer_manifest_rows = 4
    outer_manifest_self_excluding = $true
    source_payload_files = 199
    source_payload_bytes = 6911184
    source_payload_manifest_rows = 198
    source_payload_manifest_sha256 =
        '2F78F112B9F5A368725E56AD432B13EAE9B8EE08052AC3B699C0A22452EE6DC8'
    source_payload_privacy_hits = 0
    source_payload_pngs = 128
    source_payload_pngs_new_to_predecessor = 0
    zip_file_members = 199
    zip_uncompressed_bytes = 6911184
    zip_unsafe_names = 0
    zip = [ordered]@{
        bytes = $zipIdentity.bytes
        sha256 = $zipIdentity.sha256
    }
    reader = [ordered]@{
        bytes = 2675562
        pages = 266
        sha256 =
            'B717DC08C2C77546638274C7F05266F5F24C1562999117ACF4D1874AFD79EA1D'
    }
    master_tex = [ordered]@{
        bytes = 8859
        sha256 =
            'BD31E621C52AA7228BCD82A2AF827E68BB374DCF4473CBC4CF3E7E7D34E0CCE5'
    }
    rights = [ordered]@{
        new_source_pixel_class = $false
        underlying_french_rights_grant_asserted = $false
        source_derived_diagram_caveat_retained = $true
        reinhold_comparison_lineage_attributed = $true
    }
    supersession = [ordered]@{
        replace_i_iv_reader_master_archive_only = $true
        expose_v_or_later_changed = $false
    }
}
$packageValidationText = (
    $packageValidation | ConvertTo-Json -Depth 8
) + "`n"
Write-Utf8NoBom `
    -Path (Join-Path $output 'PACKAGE_VALIDATION.json') `
    -Text $packageValidationText

$outerActual = @(
    Get-ChildItem -LiteralPath $output -File |
        Sort-Object Name |
        Select-Object -ExpandProperty Name
)
$outerExpected = @(
    'PACKAGE_VALIDATION.json',
    'README.md',
    $pdfName,
    $masterName,
    $zipName,
    'SHA256SUMS.csv'
) | Sort-Object
if (
    [string]::Join("`n", $outerActual) -cne
    [string]::Join("`n", $outerExpected)
) {
    throw 'Final outer package exact-set mismatch.'
}

[pscustomobject]@{
    status = 'PASS'
    output_root = $output
    package_files = $outerActual.Count
    zip_members = 199
    zip_uncompressed_bytes = 6911184
    zip_sha256 = $zipIdentity.sha256
    pdf_sha256 =
        'B717DC08C2C77546638274C7F05266F5F24C1562999117ACF4D1874AFD79EA1D'
    master_sha256 =
        'BD31E621C52AA7228BCD82A2AF827E68BB374DCF4473CBC4CF3E7E7D34E0CCE5'
}
