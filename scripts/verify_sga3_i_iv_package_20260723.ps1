[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$PackageRoot,

    [string]$OutputPath
)

$ErrorActionPreference = 'Stop'

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

function Read-ZipEntryText {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.Compression.ZipArchiveEntry]$Entry
    )

    $stream = $Entry.Open()
    try {
        $reader = [System.IO.StreamReader]::new(
            $stream,
            [System.Text.UTF8Encoding]::new($false, $true),
            $true,
            4096,
            $false
        )
        try {
            $reader.ReadToEnd()
        }
        finally {
            $reader.Dispose()
        }
    }
    finally {
        $stream.Dispose()
    }
}

function Add-Error {
    param([Parameter(Mandatory = $true)][string]$Message)
    $script:errors.Add($Message)
}

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$root = (Resolve-Path -LiteralPath $PackageRoot).Path
$errors = [System.Collections.Generic.List[string]]::new()
$privacyHits = [System.Collections.Generic.List[object]]::new()
$formulaHits = [System.Collections.Generic.List[object]]::new()
$jsonErrors = [System.Collections.Generic.List[object]]::new()
$csvErrors = [System.Collections.Generic.List[object]]::new()

$expectedPackageNames = @(
    'PACKAGE_VALIDATION.json',
    'README.md',
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf',
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex',
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Source_Ledgers_20260723.zip',
    'SHA256SUMS.csv'
)
$actualPackageNames = @(
    Get-ChildItem -LiteralPath $root -File |
        Sort-Object Name |
        Select-Object -ExpandProperty Name
)
if (
    [string]::Join("`n", $actualPackageNames) -cne
    [string]::Join("`n", ($expectedPackageNames | Sort-Object))
) {
    Add-Error 'Outer package exact set mismatch.'
}

$outerManifestPath = Join-Path $root 'SHA256SUMS.csv'
$outerRows = @(Import-Csv -LiteralPath $outerManifestPath)
if ($outerRows.Count -ne 4) {
    Add-Error "Expected 4 outer manifest rows, found $($outerRows.Count)."
}
$outerExpectedNames = @(
    $expectedPackageNames |
        Where-Object { $_ -notin @('PACKAGE_VALIDATION.json', 'SHA256SUMS.csv') } |
        Sort-Object
)
$outerActualNames = @($outerRows.relative_path | Sort-Object)
if (
    [string]::Join("`n", $outerExpectedNames) -cne
    [string]::Join("`n", $outerActualNames)
) {
    Add-Error 'Outer manifest path set mismatch.'
}
foreach ($row in $outerRows) {
    $path = Join-Path $root $row.relative_path
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-Error "Missing outer file: $($row.relative_path)"
        continue
    }
    $item = Get-Item -LiteralPath $path
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
    if (
        $item.Length -ne [int64]$row.bytes -or
        $hash -ne $row.sha256
    ) {
        Add-Error "Outer identity mismatch: $($row.relative_path)"
    }
}

$validationPath = Join-Path $root 'PACKAGE_VALIDATION.json'
try {
    $validation = Get-Content -LiteralPath $validationPath -Raw |
        ConvertFrom-Json
    if (
        $validation.status -ne 'PASS' -or
        @($validation.errors).Count -ne 0
    ) {
        Add-Error 'Package validation is not PASS/errors[].'
    }
}
catch {
    Add-Error "Package validation JSON parse failed: $($_.Exception.Message)"
}

$pdfPath = Join-Path $root (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf'
)
$masterPath = Join-Path $root (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex'
)
if (
    (Get-FileHash -Algorithm SHA256 -LiteralPath $pdfPath).Hash -ne
    '3BD2F1B760F63F2EB43ABFB0EA4A66ACE48906599CE24F97D67434C8390A4F35'
) {
    Add-Error 'Reader PDF hash mismatch.'
}
if (
    (Get-FileHash -Algorithm SHA256 -LiteralPath $masterPath).Hash -ne
    'BD31E621C52AA7228BCD82A2AF827E68BB374DCF4473CBC4CF3E7E7D34E0CCE5'
) {
    Add-Error 'Master TeX hash mismatch.'
}

$zipPath = Join-Path $root (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_' +
    'Source_Ledgers_20260723.zip'
)
$archive = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
    $entries = @(
        $archive.Entries |
            Where-Object { -not [string]::IsNullOrEmpty($_.Name) } |
            Sort-Object FullName
    )
    if ($entries.Count -ne 200) {
        Add-Error "Expected 200 ZIP file members, found $($entries.Count)."
    }
    $unsafe = @(
        $entries |
            Where-Object {
                $_.FullName.StartsWith('/') -or
                $_.FullName.StartsWith('\') -or
                $_.FullName -match '^[A-Za-z]:' -or
                $_.FullName -match '(^|/)\.\.(/|$)'
            }
    )
    if ($unsafe.Count -ne 0) {
        Add-Error "ZIP contains $($unsafe.Count) unsafe names."
    }

    $manifestEntry = @(
        $entries | Where-Object { $_.FullName -eq 'SHA256SUMS.csv' }
    )
    if ($manifestEntry.Count -ne 1) {
        Add-Error "Expected one ZIP manifest, found $($manifestEntry.Count)."
        $innerRows = @()
    }
    else {
        $innerRows = @(
            (Read-ZipEntryText -Entry $manifestEntry[0]) |
                ConvertFrom-Csv
        )
    }
    if ($innerRows.Count -ne 199) {
        Add-Error "Expected 199 ZIP manifest rows, found $($innerRows.Count)."
    }

    $actualContentEntries = @(
        $entries | Where-Object { $_.FullName -ne 'SHA256SUMS.csv' }
    )
    $actualNames = @($actualContentEntries.FullName | Sort-Object)
    $manifestNames = @($innerRows.relative_path | Sort-Object)
    if (
        [string]::Join("`n", $actualNames) -cne
        [string]::Join("`n", $manifestNames)
    ) {
        Add-Error 'ZIP manifest path set mismatch.'
    }

    $innerByPath = @{}
    foreach ($row in $innerRows) {
        if ($innerByPath.ContainsKey($row.relative_path)) {
            Add-Error "Duplicate ZIP manifest path: $($row.relative_path)"
        }
        $innerByPath[$row.relative_path] = $row
    }

    $textExtensions = @(
        '.tex', '.md', '.csv', '.json', '.jsonl', '.txt', '.log'
    )
    $privacyPatterns = @(
        'C:\Users\Floris',
        'C:/Users/Floris',
        'C:\IL_GitHub',
        'Papors',
        'Chatnotes',
        'Claude',
        'Codex'
    )
    foreach ($entry in $actualContentEntries) {
        $stream = $entry.Open()
        try {
            $hash = Get-StreamSha256 -Stream $stream
        }
        finally {
            $stream.Dispose()
        }
        if (-not $innerByPath.ContainsKey($entry.FullName)) {
            continue
        }
        $row = $innerByPath[$entry.FullName]
        if (
            $entry.Length -ne [int64]$row.bytes -or
            $hash -ne $row.sha256
        ) {
            Add-Error "ZIP member identity mismatch: $($entry.FullName)"
        }

        $extension = [System.IO.Path]::GetExtension(
            $entry.FullName
        ).ToLowerInvariant()
        if ($extension -notin $textExtensions) {
            continue
        }
        try {
            $text = Read-ZipEntryText -Entry $entry
        }
        catch {
            Add-Error "UTF-8 read failed: $($entry.FullName)"
            continue
        }
        foreach ($pattern in $privacyPatterns) {
            if ($text -cmatch [regex]::Escape($pattern)) {
                $privacyHits.Add([pscustomobject]@{
                    path = $entry.FullName
                    pattern = $pattern
                })
            }
        }
        if ($extension -eq '.json') {
            try {
                $null = $text | ConvertFrom-Json
            }
            catch {
                $jsonErrors.Add([pscustomobject]@{
                    path = $entry.FullName
                    error = $_.Exception.Message
                })
            }
        }
        if ($extension -eq '.csv') {
            try {
                $rows = @($text | ConvertFrom-Csv)
                foreach ($csvRow in $rows) {
                    foreach ($property in $csvRow.PSObject.Properties) {
                        if ([string]$property.Value -match '^[=+\-@]') {
                            $formulaHits.Add([pscustomobject]@{
                                path = $entry.FullName
                                column = $property.Name
                                value = [string]$property.Value
                            })
                        }
                    }
                }
            }
            catch {
                $csvErrors.Add([pscustomobject]@{
                    path = $entry.FullName
                    error = $_.Exception.Message
                })
            }
        }
    }

    $imageEntry = @(
        $entries | Where-Object {
            $_.FullName -eq 'SOURCE_IMAGE_INVENTORY.csv'
        }
    )
    if ($imageEntry.Count -ne 1) {
        Add-Error 'Missing unique source-image inventory.'
        $imageRows = @()
    }
    else {
        $imageRows = @(
            (Read-ZipEntryText -Entry $imageEntry[0]) |
                ConvertFrom-Csv
        )
    }
    $requiredImages = @(
        $imageRows | Where-Object { $_.build_required -eq 'True' }
    )
    $newPixelRows = @(
        $imageRows |
            Where-Object {
                $_.release_relation -ne
                'byte_identical_to_existing_public_predecessor_asset'
            }
    )
    if ($imageRows.Count -ne 130) {
        Add-Error "Expected 130 source-image rows, found $($imageRows.Count)."
    }
    if ($requiredImages.Count -ne 96) {
        Add-Error "Expected 96 required image rows, found $($requiredImages.Count)."
    }
    if ($newPixelRows.Count -ne 0) {
        Add-Error "Found $($newPixelRows.Count) non-predecessor image rows."
    }
}
finally {
    $archive.Dispose()
}

if ($privacyHits.Count -ne 0) {
    Add-Error "Privacy scan found $($privacyHits.Count) hits."
}
if ($formulaHits.Count -ne 0) {
    Add-Error "CSV formula-safety scan found $($formulaHits.Count) hits."
}
if ($jsonErrors.Count -ne 0) {
    Add-Error "JSON parse found $($jsonErrors.Count) errors."
}
if ($csvErrors.Count -ne 0) {
    Add-Error "CSV parse found $($csvErrors.Count) errors."
}

$result = [ordered]@{
    status = $(if ($errors.Count -eq 0) { 'PASS' } else { 'FAIL' })
    errors = @($errors)
    outer_manifest_rows = $outerRows.Count
    zip_file_members = $entries.Count
    zip_manifest_rows = $innerRows.Count
    source_image_rows = $imageRows.Count
    build_required_source_images = $requiredImages.Count
    new_source_pixel_rows = $newPixelRows.Count
    privacy_hits = $privacyHits.Count
    csv_formula_hits = $formulaHits.Count
    json_parse_errors = $jsonErrors.Count
    csv_parse_errors = $csvErrors.Count
}

if ($OutputPath) {
    $parent = Split-Path -Parent $OutputPath
    if ($parent) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    [System.IO.File]::WriteAllText(
        $OutputPath,
        (($result | ConvertTo-Json -Depth 6) + "`r`n"),
        [System.Text.UTF8Encoding]::new($false)
    )
}

$result | ConvertTo-Json -Depth 6
if ($errors.Count -ne 0) {
    exit 1
}
