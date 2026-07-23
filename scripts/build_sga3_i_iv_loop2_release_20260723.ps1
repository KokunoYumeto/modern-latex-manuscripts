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

function Get-RelativePathUnix {
    param(
        [Parameter(Mandatory = $true)][string]$BasePath,
        [Parameter(Mandatory = $true)][string]$Path
    )

    ([System.IO.Path]::GetRelativePath($BasePath, $Path)).Replace('\', '/')
}

function Copy-Tree {
    param(
        [Parameter(Mandatory = $true)][string]$Source,
        [Parameter(Mandatory = $true)][string]$Destination
    )

    Get-ChildItem -LiteralPath $Source -Recurse -File |
        Sort-Object FullName |
        ForEach-Object {
            $relative = [System.IO.Path]::GetRelativePath($Source, $_.FullName)
            $target = Join-Path $Destination $relative
            New-Item -ItemType Directory -Force -Path (
                Split-Path -Parent $target
            ) | Out-Null
            Copy-Item -LiteralPath $_.FullName -Destination $target
        }
}

function New-DeterministicZip {
    param(
        [Parameter(Mandatory = $true)][string]$Source,
        [Parameter(Mandatory = $true)][string]$ZipPath
    )

    Add-Type -AssemblyName System.IO.Compression
    Add-Type -AssemblyName System.IO.Compression.FileSystem

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

$source = (Resolve-Path -LiteralPath $SourceRoot).Path
$predecessorZip = (Resolve-Path -LiteralPath $PredecessorSourceZip).Path
$outputParent = Split-Path -Parent $OutputRoot
New-Item -ItemType Directory -Force -Path $outputParent | Out-Null
if (Test-Path -LiteralPath $OutputRoot) {
    throw "Output root already exists: $OutputRoot"
}
New-Item -ItemType Directory -Path $OutputRoot | Out-Null
$output = (Resolve-Path -LiteralPath $OutputRoot).Path

$stage = Join-Path $source 'stages\reference_v2_post_loop2_r2'
$pdf = Join-Path $source (
    'build_reference_v2_post_loop2_r2\' +
    'SGA3_English_Loop1_Through_ExposeIV_Loop2_ReferenceV2_R2.pdf'
)
$master = Join-Path $stage 'tex\SGA3_English_Loop1.tex'
$finalValidation = Join-Path $source 'control\FINAL_LOCAL_VALIDATION.json'

Assert-Identity `
    -Path $pdf `
    -Bytes 2675569 `
    -Sha256 '3BD2F1B760F63F2EB43ABFB0EA4A66ACE48906599CE24F97D67434C8390A4F35'
Assert-Identity `
    -Path $master `
    -Bytes 8859 `
    -Sha256 'BD31E621C52AA7228BCD82A2AF827E68BB374DCF4473CBC4CF3E7E7D34E0CCE5'

$validation = Get-Content -LiteralPath $finalValidation -Raw |
    ConvertFrom-Json
if ($validation.status -ne 'PASS' -or @($validation.errors).Count -ne 0) {
    throw 'Final local validation is not PASS/errors[].'
}

$stageFiles = @(
    Get-ChildItem -LiteralPath $stage -Recurse -File |
        Sort-Object FullName
)
$stageBytes = [int64](
    $stageFiles | Measure-Object -Property Length -Sum
).Sum
if ($stageFiles.Count -ne 187 -or $stageBytes -ne 3361072) {
    throw "Unexpected source stage: $($stageFiles.Count) files / $stageBytes bytes."
}

$privacyPatterns = @(
    'C:\\Users\\Floris',
    'C:/Users/Floris',
    'C:\\IL_GitHub',
    'Papors',
    'Chatnotes',
    'Claude',
    'Codex'
)
$privacyHits = [System.Collections.Generic.List[object]]::new()
$textExtensions = @('.tex', '.md', '.csv', '.json', '.jsonl', '.txt', '.log')
foreach ($file in $stageFiles) {
    if ($file.Extension.ToLowerInvariant() -notin $textExtensions) {
        continue
    }
    $text = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($pattern in $privacyPatterns) {
        if ($text -cmatch [regex]::Escape($pattern)) {
            $privacyHits.Add([pscustomobject]@{
                path = Get-RelativePathUnix -BasePath $stage -Path $file.FullName
                pattern = $pattern
            })
        }
    }
}
if ($privacyHits.Count -ne 0) {
    throw "Source stage privacy scan found $($privacyHits.Count) hits."
}

# Prove that every source-stage PNG was already present byte-identically in
# the immutable public predecessor source ZIP. This release does not introduce
# a new source-pixel class.
$predecessorPngHashes = [System.Collections.Generic.HashSet[string]]::new(
    [System.StringComparer]::OrdinalIgnoreCase
)
$predecessorArchive = [System.IO.Compression.ZipFile]::OpenRead($predecessorZip)
try {
    foreach ($entry in $predecessorArchive.Entries) {
        if (
            [string]::IsNullOrEmpty($entry.Name) -or
            -not $entry.FullName.EndsWith('.png', [StringComparison]::OrdinalIgnoreCase)
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

$stagePngs = @($stageFiles | Where-Object { $_.Extension -eq '.png' })
if ($stagePngs.Count -ne 130) {
    throw "Expected 130 source-stage PNGs, found $($stagePngs.Count)."
}
foreach ($png in $stagePngs) {
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $png.FullName).Hash
    if (-not $predecessorPngHashes.Contains($hash)) {
        throw "New source-pixel identity is not in predecessor ZIP: $($png.FullName)"
    }
}

$pdfName = (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_20260723.pdf'
)
$masterName = (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_Master_20260723.tex'
)
$zipName = (
    'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_' +
    'Source_Ledgers_20260723.zip'
)

Copy-Item -LiteralPath $pdf -Destination (Join-Path $output $pdfName)
Copy-Item -LiteralPath $master -Destination (Join-Path $output $masterName)

$tempBase = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
$tempRoot = Join-Path $tempBase (
    'sga3-i-iv-loop2-release-' + [Guid]::NewGuid().ToString('N')
)
New-Item -ItemType Directory -Path $tempRoot | Out-Null
try {
    $zipStage = Join-Path $tempRoot 'zip'
    New-Item -ItemType Directory -Path $zipStage | Out-Null

    Copy-Tree -Source $stage -Destination (Join-Path $zipStage 'source')

    $referenceDir = Join-Path $zipStage 'reference_graph'
    New-Item -ItemType Directory -Path $referenceDir | Out-Null
    $ledgerRoot = Join-Path $source 'ledgers\generation_post_loop2_rebased_r2'
    foreach ($name in @(
        'REFERENCE_TARGETS.csv',
        'REFERENCE_CANDIDATES.csv',
        'REFERENCE_EDGES.csv',
        'REFERENCE_RESIDUALS.csv',
        'REFERENCE_SET_RELATION.json'
    )) {
        Copy-Item `
            -LiteralPath (Join-Path $ledgerRoot $name) `
            -Destination (Join-Path $referenceDir $name)
    }

    $evidenceDir = Join-Path $zipStage 'evidence'
    New-Item -ItemType Directory -Path $evidenceDir | Out-Null
    $evidenceMap = [ordered]@{
        'control\FINAL_LOCAL_VALIDATION.json' =
            'FINAL_LOCAL_VALIDATION.json'
        'control\reference_pdf_action_audit_post_loop2_r2\REFERENCE_PDF_AUDIT.json' =
            'REFERENCE_PDF_AUDIT.json'
        'control\reference_pdf_action_audit_post_loop2_r2\REFERENCE_PDF_AUDIT_PASS.md' =
            'REFERENCE_PDF_AUDIT_PASS.md'
        'control\independent_reference_graph_audit_post_loop2_r2\INDEPENDENT_AUDIT_RECEIPT.md' =
            'INDEPENDENT_REFERENCE_GRAPH_AUDIT_PASS.md'
        'control\final_linked_visual_qa_r2\FINAL_LINKED_VISUAL_QA_RECEIPT.md' =
            'FINAL_LINKED_VISUAL_QA_RECEIPT.md'
    }
    foreach ($relative in $evidenceMap.Keys) {
        Copy-Item `
            -LiteralPath (Join-Path $source $relative) `
            -Destination (Join-Path $evidenceDir $evidenceMap[$relative])
    }

    $texText = (
        Get-ChildItem -LiteralPath (Join-Path $stage 'tex') -Recurse -Filter *.tex |
            Get-Content -Raw
    ) -join "`n"
    $requiredPngs = [System.Collections.Generic.HashSet[string]]::new(
        [System.StringComparer]::OrdinalIgnoreCase
    )
    foreach ($match in [regex]::Matches(
        $texText,
        '\{((?:figures|assets)/[^}\r\n]+\.png)\}'
    )) {
        if ($match.Groups[1].Value -ne 'figures/exp1/diagram-id.png') {
            [void]$requiredPngs.Add($match.Groups[1].Value)
        }
    }
    if ($requiredPngs.Count -ne 96) {
        throw "Expected 96 build-required PNGs, found $($requiredPngs.Count)."
    }

    $imageRows = foreach ($png in $stagePngs | Sort-Object FullName) {
        $relative = Get-RelativePathUnix -BasePath $stage -Path $png.FullName
        $identity = Get-Identity -Path $png.FullName
        [pscustomobject][ordered]@{
            relative_path = $relative
            bytes = $identity.bytes
            sha256 = $identity.sha256
            build_required = $requiredPngs.Contains($relative)
            release_relation = 'byte_identical_to_existing_public_predecessor_asset'
            rights_status = 'underlying_french_rights_not_granted_retain_caveat'
        }
    }
    $imageCsv = (($imageRows | ConvertTo-Csv -NoTypeInformation) -join "`r`n") +
        "`r`n"
    Write-Utf8NoBom `
        -Path (Join-Path $zipStage 'SOURCE_IMAGE_INVENTORY.csv') `
        -Text $imageCsv

    $releaseNote = @'
# SGA 3 English through Expose IV: Loop2/reference-v2 R2

This package accompanies the cumulative 266-page English working reader
through the end of Expose IV. Expose V is published separately; Exposes VI-XXVI
are not included here.

The Expose IV portion has complete native TeX diagram reconstruction and a
closed convention-v2 graph: 411 targets, 1,157 candidates/residuals, and 611
linked edges. The compiled PDF has 1,519 named destinations and 1,062 internal
GoTo rectangles. The final three-pass build, independent graph audit, PDF
action/font/text audit, and rendered visual QA all pass.

The 130 PNG assets in the source stage are byte-identical to assets already
published in the predecessor cumulative-through-Expose-III source package.
Ninety-six are needed by that inherited Loop1 build; thirty-four are retained
recovery/QA assets. Expose IV uses native TeX diagrams and adds no new source
pixels. The image inventory records every identity and its build role.

The controlling Expose IV authority is the Polo-Gille current reader,
SHA-256 7126C52925A0CC320F28D68B139B6763EEACD59ED8907714B4AD7CA8C6C14D5D.
OCR and external English material were locator/comparison material only.
Jacob C. Reinhold's jcreinhold/sga snapshot
e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited comparison/drafting
lineage, not authority. Reinhold states CC BY 4.0 for his translation
contribution only.

No new rights grant is asserted for the underlying French work or inherited
source-derived diagram pixels. This is a machine-assisted working translation
and reconstruction, not a critical edition, mathematical certification,
independent human peer review, rights determination, accessibility
certification, or complete SGA 3.
'@
    Write-Utf8NoBom `
        -Path (Join-Path $zipStage 'PUBLIC_RELEASE_NOTE.md') `
        -Text ($releaseNote.Trim() + "`r`n")

    $zipMemberFiles = @(
        Get-ChildItem -LiteralPath $zipStage -Recurse -File |
            Sort-Object {
                Get-RelativePathUnix -BasePath $zipStage -Path $_.FullName
            }
    )
    $zipManifestRows = foreach ($file in $zipMemberFiles) {
        $identity = Get-Identity -Path $file.FullName
        [pscustomobject][ordered]@{
            relative_path = Get-RelativePathUnix `
                -BasePath $zipStage `
                -Path $file.FullName
            bytes = $identity.bytes
            sha256 = $identity.sha256
        }
    }
    $zipManifest = (
        ($zipManifestRows | ConvertTo-Csv -NoTypeInformation) -join "`r`n"
    ) + "`r`n"
    Write-Utf8NoBom `
        -Path (Join-Path $zipStage 'SHA256SUMS.csv') `
        -Text $zipManifest

    $zipPath = Join-Path $output $zipName
    New-DeterministicZip -Source $zipStage -ZipPath $zipPath
}
finally {
    $resolvedTemp = [System.IO.Path]::GetFullPath($tempRoot)
    if (-not $resolvedTemp.StartsWith(
        $tempBase,
        [System.StringComparison]::OrdinalIgnoreCase
    )) {
        throw "Refusing to remove unexpected temporary path: $resolvedTemp"
    }
    Remove-Item -LiteralPath $resolvedTemp -Recurse -Force
}

$readme = @"
# SGA 3 English through Expose IV - Loop2/reference-v2 R2

This compact archive package publishes the cumulative English working reader
through complete Expose IV.

- Reader: 266 A4 pages.
- Scope: Editorial Notice, Introduction, and complete Exposes I-IV.
- Expose IV Loop2: native TeX diagrams complete.
- Reference-v2 graph: 411 targets, 1,157 candidate/residual occurrences, and
  611 linked edges.
- PDF: 1,519 named destinations and 1,062 internal GoTo rectangles.
- Expose V is a separate bounded reader.
- Exposes VI-XXVI are not included.

The source ZIP contains the exact 187-file privacy-clean source stage, the
reference graph, compact build/PDF/visual audit receipts, and an image
inventory. Its 130 PNG assets are byte-identical to the already-public
predecessor I-III package; Expose IV adds no source pixels and uses native TeX
diagrams.

Authority, attribution, and rights caveats are stated inside the ZIP. No new
license or underlying-French rights grant is asserted. This is a working
translation/reconstruction, not a complete SGA 3 or critical edition.
"@
Write-Utf8NoBom `
    -Path (Join-Path $output 'README.md') `
    -Text ($readme.Trim() + "`r`n")

$outerContent = @(
    Get-Item -LiteralPath (Join-Path $output 'README.md')
    Get-Item -LiteralPath (Join-Path $output $pdfName)
    Get-Item -LiteralPath (Join-Path $output $masterName)
    Get-Item -LiteralPath (Join-Path $output $zipName)
) | Sort-Object Name
$outerRows = foreach ($file in $outerContent) {
    $identity = Get-Identity -Path $file.FullName
    [pscustomobject][ordered]@{
        relative_path = $file.Name
        bytes = $identity.bytes
        sha256 = $identity.sha256
    }
}
$outerManifest = (($outerRows | ConvertTo-Csv -NoTypeInformation) -join "`r`n") +
    "`r`n"
$outerManifestPath = Join-Path $output 'SHA256SUMS.csv'
Write-Utf8NoBom -Path $outerManifestPath -Text $outerManifest

$zipCheck = [System.IO.Compression.ZipFile]::OpenRead((Join-Path $output $zipName))
try {
    $zipEntries = @(
        $zipCheck.Entries |
            Where-Object { -not [string]::IsNullOrEmpty($_.Name) }
    )
    $zipBytes = [int64](
        $zipEntries | Measure-Object -Property Length -Sum
    ).Sum
    $badNames = @(
        $zipEntries |
            Where-Object {
                $_.FullName.StartsWith('/') -or
                $_.FullName.StartsWith('\') -or
                $_.FullName -match '^[A-Za-z]:' -or
                $_.FullName -match '(^|/)\.\.(/|$)'
            }
    )
    if ($badNames.Count -ne 0) {
        throw "ZIP contains $($badNames.Count) unsafe names."
    }
}
finally {
    $zipCheck.Dispose()
}

$packageFiles = @(
    Get-ChildItem -LiteralPath $output -File |
        Sort-Object Name
)
$packageBytes = [int64](
    $packageFiles | Measure-Object -Property Length -Sum
).Sum
$validationObject = [ordered]@{
    status = 'PASS'
    errors = @()
    scope = 'SGA3 cumulative English working reader through Expose IV'
    source_root_mutated = $false
    package_files = $packageFiles.Count + 1
    package_bytes_excluding_validation = $packageBytes
    outer_manifest_rows = $outerRows.Count
    outer_manifest_self_excluding = $true
    source_stage_files = $stageFiles.Count
    source_stage_bytes = $stageBytes
    source_stage_privacy_hits = $privacyHits.Count
    source_stage_pngs = $stagePngs.Count
    source_stage_pngs_new_to_predecessor = 0
    build_required_pngs = $requiredPngs.Count
    zip_file_members = $zipEntries.Count
    zip_uncompressed_bytes = $zipBytes
    zip_unsafe_names = $badNames.Count
    reader = [ordered]@{
        bytes = 2675569
        pages = 266
        sha256 = '3BD2F1B760F63F2EB43ABFB0EA4A66ACE48906599CE24F97D67434C8390A4F35'
    }
    master_tex = [ordered]@{
        bytes = 8859
        sha256 = 'BD31E621C52AA7228BCD82A2AF827E68BB374DCF4473CBC4CF3E7E7D34E0CCE5'
    }
    rights = [ordered]@{
        new_source_pixel_class = $false
        underlying_french_rights_grant_asserted = $false
        reinhold_comparison_lineage_attributed = $true
    }
}
$validationPath = Join-Path $output 'PACKAGE_VALIDATION.json'
Write-Utf8NoBom `
    -Path $validationPath `
    -Text (
        ($validationObject | ConvertTo-Json -Depth 8) + "`r`n"
    )

$finalFiles = @(Get-ChildItem -LiteralPath $output -File)
$finalBytes = [int64](
    $finalFiles | Measure-Object -Property Length -Sum
).Sum
Write-Output (
    "PASS package={0} files={1} bytes={2} zip_members={3} zip_bytes={4}" -f
    $output,
    $finalFiles.Count,
    $finalBytes,
    $zipEntries.Count,
    $zipBytes
)
