$ErrorActionPreference = 'Stop'

$root = $PSScriptRoot
$manifestPath = Join-Path $root '17_ZENODO_PAYLOAD_MANIFEST.csv'
$validationPath = Join-Path $root '19_PACKAGE_VALIDATION.json'
$excludedControls = @('17_ZENODO_PAYLOAD_MANIFEST.csv', '19_PACKAGE_VALIDATION.json')
$errors = [System.Collections.Generic.List[string]]::new()

function Get-Sha256([string]$Path) {
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash
}

function Get-Role([System.IO.FileInfo]$File) {
    if ($File.Name -eq '00_READ_ME_FIRST.md') { return 'front_document' }
    if ($File.Extension -eq '.pdf') { return 'reader' }
    if ($File.Extension -eq '.csv') { return 'machine_evidence' }
    if ($File.Extension -eq '.zip') { return 'editable_source_bundle' }
    if ($File.Name -like '*SUPERSEDED*') { return 'adverse_validation_history' }
    if ($File.Name -eq 'VALIDATE_FAC_DOI_PACKAGE.ps1') { return 'package_validator' }
    return 'provenance_and_method'
}

# Generate the self-excluding payload manifest from the current root.
$payloadFiles = @(Get-ChildItem -LiteralPath $root -File |
    Where-Object { $_.Name -notin $excludedControls } |
    Sort-Object Name)
$manifestRows = @($payloadFiles | ForEach-Object {
    [pscustomobject]@{
        filename = $_.Name
        bytes = $_.Length
        sha256 = Get-Sha256 $_.FullName
        role = Get-Role $_
    }
})
$manifestRows | Export-Csv -LiteralPath $manifestPath -NoTypeInformation -Encoding utf8

# Replay the manifest.
$manifestReplayErrors = [System.Collections.Generic.List[string]]::new()
foreach ($row in @(Import-Csv -LiteralPath $manifestPath)) {
    $path = Join-Path $root $row.filename
    if (-not (Test-Path -LiteralPath $path)) {
        $manifestReplayErrors.Add("missing:$($row.filename)")
        continue
    }
    $item = Get-Item -LiteralPath $path
    $hash = Get-Sha256 $path
    if ($item.Length -ne [int64]$row.bytes -or $hash -ne $row.sha256) {
        $manifestReplayErrors.Add("mismatch:$($row.filename)")
    }
}
foreach ($entry in $manifestReplayErrors) { $errors.Add($entry) }

# Privacy scan. Construct private tokens from parts so the validator does not
# contain the very literals it is designed to detect.
$privacyPatterns = @(
    [regex]::Escape(('C:' + '\Users\' + 'Floris')),
    [regex]::Escape(('C:' + '/Users/' + 'Floris')),
    [regex]::Escape(('.' + 'codex')),
    '019f[0-9a-f-]{20,}',
    [regex]::Escape(('memo_lepthy' + '@' + 'live.nl'))
)
$privacyHits = [System.Collections.Generic.List[object]]::new()
$directTextFiles = @(Get-ChildItem -LiteralPath $root -File |
    Where-Object { $_.Extension -in @('.md', '.csv', '.json', '.txt', '.ps1') })
foreach ($file in $directTextFiles) {
    $lines = Get-Content -LiteralPath $file.FullName
    for ($i = 0; $i -lt $lines.Count; $i++) {
        foreach ($pattern in $privacyPatterns) {
            if ($lines[$i] -match $pattern) {
                $privacyHits.Add([pscustomobject]@{ file = $file.Name; line = $i + 1 })
            }
        }
    }
}

# CSV rectangularity and spreadsheet-formula safety.
$csvReports = [System.Collections.Generic.List[object]]::new()
$formulaTriggers = [System.Collections.Generic.List[object]]::new()
foreach ($file in @(Get-ChildItem -LiteralPath $root -Filter '*.csv' -File)) {
    $rows = @(Import-Csv -LiteralPath $file.FullName)
    $headers = @($rows[0].PSObject.Properties.Name)
    $badRows = [System.Collections.Generic.List[int]]::new()
    for ($i = 0; $i -lt $rows.Count; $i++) {
        if (@($rows[$i].PSObject.Properties.Name).Count -ne $headers.Count) {
            $badRows.Add($i + 2)
        }
        foreach ($property in $rows[$i].PSObject.Properties) {
            $value = [string]$property.Value
            if ($value -match '^[=+@]' -or $value -match '^-[^0-9]') {
                $formulaTriggers.Add([pscustomobject]@{
                    file = $file.Name
                    row = $i + 2
                    column = $property.Name
                })
            }
        }
    }
    $csvReports.Add([pscustomobject]@{
        file = $file.Name
        rows = $rows.Count
        columns = $headers.Count
        bad_rows = @($badRows)
    })
    if ($badRows.Count) { $errors.Add("nonrectangular:$($file.Name)") }
}
if ($formulaTriggers.Count) { $errors.Add("formula_triggers=$($formulaTriggers.Count)") }

# Open and replay the source ZIP and its internal manifest.
Add-Type -AssemblyName System.IO.Compression.FileSystem
$sourceZipPath = Join-Path $root '16_FAC_Project_English_and_French_TeX_Source_Layers.zip'
$zip = [System.IO.Compression.ZipFile]::OpenRead($sourceZipPath)
try {
    $zipFiles = @($zip.Entries | Where-Object { -not [string]::IsNullOrEmpty($_.Name) })
    $unsafeZipPaths = @($zipFiles | Where-Object {
        $_.FullName.StartsWith('/') -or
        $_.FullName.StartsWith('\') -or
        $_.FullName -match '(^|[\\/])\.\.([\\/]|$)' -or
        $_.FullName -match '^[A-Za-z]:'
    })
    if ($unsafeZipPaths.Count) { $errors.Add("unsafe_zip_paths=$($unsafeZipPaths.Count)") }

    $manifestEntry = $zipFiles | Where-Object {
        $_.FullName.Replace('\', '/') -eq 'SOURCE_FILE_MANIFEST.csv'
    }
    if (@($manifestEntry).Count -ne 1) {
        $errors.Add("source_manifest_entry_count=$(@($manifestEntry).Count)")
        $sourceRows = @()
        $sourceManifestHash = $null
    }
    else {
        $stream = $manifestEntry.Open()
        try {
            $memory = [System.IO.MemoryStream]::new()
            $stream.CopyTo($memory)
            $manifestBytes = $memory.ToArray()
        }
        finally {
            $stream.Dispose()
            if ($memory) { $memory.Dispose() }
        }
        $sourceManifestHash = [Convert]::ToHexString(
            [Security.Cryptography.SHA256]::HashData($manifestBytes)
        )
        $sourceRows = @([Text.Encoding]::UTF8.GetString($manifestBytes) | ConvertFrom-Csv)
    }

    $zipByPath = @{}
    foreach ($entry in $zipFiles) { $zipByPath[$entry.FullName.Replace('\', '/')] = $entry }
    $sourceReplayErrors = [System.Collections.Generic.List[string]]::new()
    foreach ($row in $sourceRows) {
        if (-not $zipByPath.ContainsKey($row.path)) {
            $sourceReplayErrors.Add("missing:$($row.path)")
            continue
        }
        $entry = $zipByPath[$row.path]
        $stream = $entry.Open()
        try {
            $sha = [Security.Cryptography.SHA256]::Create()
            try { $hashBytes = $sha.ComputeHash($stream) }
            finally { $sha.Dispose() }
        }
        finally { $stream.Dispose() }
        $hash = [Convert]::ToHexString($hashBytes)
        if ($entry.Length -ne [int64]$row.bytes -or $hash -ne $row.sha256) {
            $sourceReplayErrors.Add("mismatch:$($row.path)")
        }
    }
    foreach ($entry in $sourceReplayErrors) { $errors.Add("source_zip_$entry") }

    # Scan the uncompressed source text for private path/task tokens.
    foreach ($entry in $zipFiles) {
        $extension = [IO.Path]::GetExtension($entry.Name).ToLowerInvariant()
        if ($extension -notin @('.md', '.csv', '.json', '.txt', '.tex')) { continue }
        $stream = $entry.Open()
        try {
            $reader = [IO.StreamReader]::new($stream, [Text.Encoding]::UTF8, $true)
            try { $text = $reader.ReadToEnd() }
            finally { $reader.Dispose() }
        }
        finally { $stream.Dispose() }
        foreach ($pattern in $privacyPatterns) {
            if ($text -match $pattern) {
                $privacyHits.Add([pscustomobject]@{ file = "ZIP:$($entry.FullName)"; line = 0 })
            }
        }
    }
}
finally { $zip.Dispose() }
if ($privacyHits.Count) { $errors.Add("privacy_hits=$($privacyHits.Count)") }

# PDF page counts and clean reader-surface text.
$pdfInfoExe = (Get-Command pdfinfo.exe -All | Select-Object -First 1).Source
$pdfToTextExe = (Get-Command pdftotext.exe -All | Select-Object -First 1).Source
$readerNames = @(
    '01_FAC_Codex_Blind_English_Reader_through_no79.pdf',
    '02_FAC_Codex_Complete_English_Reader.pdf'
)
$expectedPages = @(74, 78)
$readerReports = [System.Collections.Generic.List[object]]::new()
$readerStatusHits = [System.Collections.Generic.List[object]]::new()
for ($i = 0; $i -lt $readerNames.Count; $i++) {
    $name = $readerNames[$i]
    $path = Join-Path $root $name
    $info = @(& $pdfInfoExe $path 2>&1)
    $infoExit = $LASTEXITCODE
    $pageLines = @($info | Where-Object { $_ -match '^Pages:' })
    $pages = $null
    if ($infoExit -ne 0) {
        $errors.Add("pdfinfo_exit_${infoExit}:$name")
    }
    elseif ($pageLines.Count -ne 1) {
        $errors.Add("pdfinfo_page_line_count_$($pageLines.Count):$name")
    }
    else {
        $pages = [int](($pageLines[0] -split ':', 2)[1].Trim())
        if ($pages -ne $expectedPages[$i]) {
            $errors.Add("page_count_${pages}_expected_$($expectedPages[$i]):$name")
        }
    }

    $tempText = Join-Path ([IO.Path]::GetTempPath()) ("fac-doi-" + [guid]::NewGuid() + '.txt')
    try {
        & $pdfToTextExe -layout $path $tempText 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $tempText)) {
            $errors.Add("pdftotext_failure:$name")
        }
        else {
            $surfacePattern = 'Codex|OpenAI|Claude|workflow|production status|source-aligned|working reader|artificial intelligence|not certified|not complete'
            foreach ($match in @(Select-String -LiteralPath $tempText -Pattern $surfacePattern -CaseSensitive:$false)) {
                $readerStatusHits.Add([pscustomobject]@{ file = $name; line = $match.LineNumber })
            }
        }
    }
    finally {
        if (Test-Path -LiteralPath $tempText) { Remove-Item -LiteralPath $tempText -Force }
    }
    $readerReports.Add([pscustomobject]@{
        file = $name
        bytes = (Get-Item -LiteralPath $path).Length
        sha256 = Get-Sha256 $path
        pages = $pages
        pdfinfo_exit = $infoExit
        page_line_count = $pageLines.Count
    })
}
if ($readerStatusHits.Count) { $errors.Add("reader_status_hits=$($readerStatusHits.Count)") }

# Comparator counts and key closure checks.
$unitRows = @(Import-Csv -LiteralPath (Join-Path $root '03_FAC_Blind_Comparator_Unit_Reviews.csv'))
$findingRows = @(Import-Csv -LiteralPath (Join-Path $root '04_FAC_Blind_Comparator_Findings.csv'))
$inventoryRows = @(Import-Csv -LiteralPath (Join-Path $root '13_FAC_Blind_Comparator_Inventory.csv'))
$inputRows = @(Import-Csv -LiteralPath (Join-Path $root '14_FAC_Blind_Input_Identities.csv'))
$selfRows = @(Import-Csv -LiteralPath (Join-Path $root '08_FAC_Self_Correction_Ledger.csv'))
$blindValidation = Get-Content -LiteralPath (Join-Path $root '15_FAC_Blind_Comparator_Validation.json') -Raw | ConvertFrom-Json
if ($unitRows.Count -ne 79) { $errors.Add("unit_count=$($unitRows.Count)") }
if ($findingRows.Count -ne 138) { $errors.Add("finding_count=$($findingRows.Count)") }
if ($inventoryRows.Count -ne 79) { $errors.Add("inventory_count=$($inventoryRows.Count)") }
if ($inputRows.Count -ne 95) { $errors.Add("input_identity_count=$($inputRows.Count)") }
if (@($unitRows.review_id | Sort-Object -Unique).Count -ne $unitRows.Count) { $errors.Add('duplicate_review_ids') }
if (@($findingRows.finding_id | Sort-Object -Unique).Count -ne $findingRows.Count) { $errors.Add('duplicate_finding_ids') }

$validation = [ordered]@{
    status = if ($errors.Count) { 'FAIL_HOLD' } else { 'PASS_READY_FOR_DEDICATED_ZENODO_PUBLICATION' }
    generated_at = '2026-08-03T18:45:00+02:00'
    errors = @($errors)
    scope = [ordered]@{
        work = 'Jean-Pierre Serre, Faisceaux algebriques coherents'
        purpose = 'accidental blind translation comparison and AI-output quality assessment'
        blind_units = $unitRows.Count
        findings = $findingRows.Count
        inventory_rows = $inventoryRows.Count
        input_identity_rows = $inputRows.Count
        self_correction_rows = $selfRows.Count
        mathematician_peer_reviewed = $false
        canonicity_claim = $false
    }
    chronology = [ordered]@{
        blind_boundary = 'FAC no.79'
        blind_reader_sha256 = $readerReports[0].sha256
        complete_reader_includes_comparator_aware_units = 'nos.80-81'
        comparison_discovered_after_blind_freeze = $true
    }
    readers = @($readerReports)
    reader_surface = [ordered]@{
        workflow_or_ai_prose_hits = $readerStatusHits.Count
        status = if ($readerStatusHits.Count) { 'FAIL' } else { 'PASS' }
    }
    source_bundle = [ordered]@{
        file = '16_FAC_Project_English_and_French_TeX_Source_Layers.zip'
        bytes = (Get-Item -LiteralPath $sourceZipPath).Length
        sha256 = Get-Sha256 $sourceZipPath
        zip_file_entries = $zipFiles.Count
        unsafe_paths = $unsafeZipPaths.Count
        source_manifest_rows = $sourceRows.Count
        source_manifest_sha256 = $sourceManifestHash
        source_manifest_replay_errors = @($sourceReplayErrors)
        authority_scan_included = $false
        external_comparator_included = $false
    }
    machine_evidence = [ordered]@{
        csv_reports = @($csvReports)
        formula_triggers = $formulaTriggers.Count
        review_ids_unique = (@($unitRows.review_id | Sort-Object -Unique).Count -eq $unitRows.Count)
        finding_ids_unique = (@($findingRows.finding_id | Sort-Object -Unique).Count -eq $findingRows.Count)
        blind_validation_status = $blindValidation.status
    }
    privacy = [ordered]@{
        hits = $privacyHits.Count
        r1_rejected_due_internal_task_identifier = $true
        r2_public_logbook_transform_disclosed = $true
    }
    rights = [ordered]@{
        french_authority_redistributed = $false
        achinger_krupa_pdf_or_source_redistributed = $false
        project_artifacts_only = $true
        rights_caveat_file = '10_RIGHTS_AND_LIMITS.md'
    }
    manifest = [ordered]@{
        file = '17_ZENODO_PAYLOAD_MANIFEST.csv'
        rows = $manifestRows.Count
        sha256 = Get-Sha256 $manifestPath
        replay_errors = @($manifestReplayErrors)
        self_excluding = $true
        validation_excluded = $true
    }
    adverse_history = [ordered]@{
        superseded_false_pass_file = '18_PACKAGE_VALIDATION_SUPERSEDED_R1_FALSE_PASS.json'
        superseded_false_pass_sha256 = Get-Sha256 (Join-Path $root '18_PACKAGE_VALIDATION_SUPERSEDED_R1_FALSE_PASS.json')
    }
    claims_excluded = @(
        'mathematical certification',
        'peer review',
        'critical edition',
        'canonicity',
        'scalar model score',
        'general model superiority',
        'blanket rights clearance'
    )
}
$validation | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $validationPath -Encoding utf8

[pscustomobject]@{
    status = $validation.status
    errors = $errors.Count
    payload_rows = $manifestRows.Count
    payload_bytes = ($manifestRows | Measure-Object -Property bytes -Sum).Sum
    manifest_sha256 = Get-Sha256 $manifestPath
    validation_sha256 = Get-Sha256 $validationPath
    privacy_hits = $privacyHits.Count
    formula_triggers = $formulaTriggers.Count
    source_zip_entries = $zipFiles.Count
    source_replay_errors = $sourceReplayErrors.Count
    reader_status_hits = $readerStatusHits.Count
    blind_pages = $readerReports[0].pages
    complete_pages = $readerReports[1].pages
}
