param()

$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$FrenchAuthority = Join-Path $Root 'authority\sga5_fr_workpass.tex'
$ExpectedFrenchSha256 = '791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28'
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Get-Sha256Bytes([byte[]]$Bytes) {
    $Hasher = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([BitConverter]::ToString($Hasher.ComputeHash($Bytes))).Replace('-', '')
    }
    finally {
        $Hasher.Dispose()
    }
}

function Get-NormalizedText([string]$Path) {
    $Text = [IO.File]::ReadAllText($Path)
    return $Text.Replace("`r`n", "`n").Replace("`r", "`n")
}

function Expand-TexInputs([string]$Path, [System.Collections.Generic.HashSet[string]]$Stack) {
    $Resolved = [IO.Path]::GetFullPath($Path)
    if (-not $Stack.Add($Resolved)) {
        throw "Recursive TeX input detected at $Resolved"
    }
    try {
        $Text = Get-NormalizedText $Resolved
        $Base = Split-Path -Parent $Resolved
        return [regex]::Replace($Text, '\\input\{([^}]+)\}', {
            param($Match)
            $Child = $Match.Groups[1].Value
            if (-not [IO.Path]::HasExtension($Child)) {
                $Child += '.tex'
            }
            $ChildPath = Join-Path $Base $Child
            if (-not (Test-Path -LiteralPath $ChildPath)) {
                throw "Missing TeX input: $ChildPath"
            }
            return Expand-TexInputs $ChildPath $Stack
        })
    }
    finally {
        [void]$Stack.Remove($Resolved)
    }
}

function Escape-Csv([object]$Value) {
    $Text = [string]$Value
    return '"' + $Text.Replace('"', '""') + '"'
}

Push-Location $Root
try {
    $AuthorityHash = (Get-FileHash -LiteralPath $FrenchAuthority -Algorithm SHA256).Hash
    if ($AuthorityHash -ne $ExpectedFrenchSha256) {
        throw "French authority hash drift: expected $ExpectedFrenchSha256, got $AuthorityHash"
    }

    $Stack = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    $Expanded = Expand-TexInputs (Join-Path $Root 'sga5_es.tex') $Stack
    $TargetDocumentSha256 = Get-Sha256Bytes $Utf8NoBom.GetBytes($Expanded)
    $Parity = Import-Csv -LiteralPath (Join-Path $Root 'evidence\UNIT_PARITY.csv')
    $FrenchLines = [IO.File]::ReadAllLines($FrenchAuthority)
    $Rows = New-Object System.Collections.Generic.List[object]

    foreach ($Unit in $Parity) {
        if ($Unit.source_lines -notmatch '^(\d+)-(\d+)$') {
            throw "Invalid source line range for $($Unit.unit_id): $($Unit.source_lines)"
        }
        $Start = [int]$Matches[1]
        $End = [int]$Matches[2]
        if ($Start -lt 1 -or $End -lt $Start -or $End -gt $FrenchLines.Count) {
            throw "Out-of-range source span for $($Unit.unit_id): $Start-$End"
        }
        $SourceUnit = (($FrenchLines[($Start - 1)..($End - 1)] -join "`n") + "`n")
        $TargetPath = Join-Path $Root $Unit.target_path
        if (-not (Test-Path -LiteralPath $TargetPath)) {
            throw "Missing target unit: $TargetPath"
        }
        $Rows.Add([pscustomobject][ordered]@{
            unit_id = $Unit.unit_id
            source_document_sha256 = $AuthorityHash
            source_lines = $Unit.source_lines
            source_unit_sha256_lf = Get-Sha256Bytes $Utf8NoBom.GetBytes($SourceUnit)
            target_path = $Unit.target_path.Replace('\\', '/')
            target_unit_sha256_raw = (Get-FileHash -LiteralPath $TargetPath -Algorithm SHA256).Hash
            target_document_sha256_expanded_lf = $TargetDocumentSha256
            status = $Unit.status
            review_evidence = $Unit.review_evidence
        })
    }

    $Header = ($Rows[0].PSObject.Properties.Name | ForEach-Object { Escape-Csv $_ }) -join ','
    $CsvLines = New-Object System.Collections.Generic.List[string]
    $CsvLines.Add($Header)
    foreach ($Row in $Rows) {
        $CsvLines.Add(($Row.PSObject.Properties.Value | ForEach-Object { Escape-Csv $_ }) -join ',')
    }
    [IO.File]::WriteAllText((Join-Path $Root 'evidence\UNIT_HASHES_CURRENT.csv'), (($CsvLines -join "`n") + "`n"), $Utf8NoBom)

    $TargetManifest = [ordered]@{
        schema = 'sga5-expanded-target-v1'
        generated_utc = [DateTime]::UtcNow.ToString('o')
        master = 'sga5_es.tex'
        expansion_rule = 'Recursively replace each literal TeX input command with the referenced UTF-8 text in input order; normalize CRLF/CR to LF; hash UTF-8 without BOM.'
        target_document_sha256 = $TargetDocumentSha256
        source_document_sha256 = $AuthorityHash
        unit_count = $Rows.Count
    }
    [IO.File]::WriteAllText((Join-Path $Root 'evidence\TARGET_DOCUMENT_CURRENT.json'), (($TargetManifest | ConvertTo-Json -Depth 4) + "`n"), $Utf8NoBom)
    Write-Output "Generated evidence for $($Rows.Count) units; expanded target SHA256 $TargetDocumentSha256"
}
finally {
    Pop-Location
}
