[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidatePattern('^GH-[0-9]{8}-[0-9]{3}$')]
    [string]$Id,

    [Parameter(Mandatory)]
    [ValidatePattern('^[0-9]{4}-[0-9]{2}-[0-9]{2}T.*Z$')]
    [string]$TimeUtc,

    [Parameter(Mandatory)]
    [ValidateSet('control', 'decision', 'error', 'correction')]
    [string]$Kind,

    [Parameter(Mandatory)]
    [string]$Decision,

    [Parameter(Mandatory)]
    [string]$Rationale,

    [string[]]$Evidence = @(),
    [string[]]$Supersedes = @(),
    [string]$LogPath = 'manifests/github-custody/log.jsonl'
)

$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false)

function Get-Hash {
    param([string]$Text)
    $sha = [Security.Cryptography.SHA256]::Create()
    try {
        return [Convert]::ToHexString($sha.ComputeHash($utf8.GetBytes($Text)))
    }
    finally {
        $sha.Dispose()
    }
}

function Get-Canonical {
    param([object]$Record)
    $ordered = [ordered]@{
        schema             = 'github-maint-log/v1'
        id                 = [string]$Record.id
        time_utc           = [string]$Record.time_utc
        kind               = [string]$Record.kind
        decision           = [string]$Record.decision
        rationale          = [string]$Record.rationale
        evidence           = @($Record.evidence)
        supersedes         = @($Record.supersedes)
        prev_record_sha256 = $Record.prev_record_sha256
    }
    return (($ordered | ConvertTo-Json -Compress -Depth 6).Replace("`r`n", "`n"))
}

$parsedTime = [DateTimeOffset]::MinValue
if (-not [DateTimeOffset]::TryParse(
    $TimeUtc,
    [Globalization.CultureInfo]::InvariantCulture,
    [Globalization.DateTimeStyles]::RoundtripKind,
    [ref]$parsedTime
)) {
    throw 'TimeUtc is not a valid round-trip timestamp.'
}

$fullPath = [IO.Path]::GetFullPath((Join-Path (Get-Location) $LogPath))
$directory = [IO.Path]::GetDirectoryName($fullPath)
if (-not [IO.Directory]::Exists($directory)) {
    throw "Log directory does not exist: $directory"
}

$stream = [IO.File]::Open(
    $fullPath,
    [IO.FileMode]::OpenOrCreate,
    [IO.FileAccess]::ReadWrite,
    [IO.FileShare]::None
)
try {
    $existingBytes = [byte[]]::new($stream.Length)
    if ($existingBytes.Length -gt 0) {
        $read = $stream.Read($existingBytes, 0, $existingBytes.Length)
        if ($read -ne $existingBytes.Length) { throw 'Could not read the complete log.' }
        if ($existingBytes.Length -ge 3 -and
            $existingBytes[0] -eq 0xEF -and
            $existingBytes[1] -eq 0xBB -and
            $existingBytes[2] -eq 0xBF) {
            throw 'The log must not contain a UTF-8 BOM.'
        }
        if ($existingBytes[-1] -ne 0x0A) { throw 'The log must end with LF.' }
    }

    $existingText = $utf8.GetString($existingBytes)
    if ($existingText.Contains("`r")) { throw 'The log must use LF, not CRLF.' }
    $lines = @($existingText.Split("`n") | Where-Object { $_.Length -gt 0 })
    $ids = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    $priorHash = $null

    foreach ($line in $lines) {
        $record = $line | ConvertFrom-Json -DateKind String
        if ($record.schema -ne 'github-maint-log/v1') { throw "Bad schema in $($record.id)." }
        if (-not $ids.Add([string]$record.id)) { throw "Duplicate ID: $($record.id)" }
        if ($record.prev_record_sha256 -ne $priorHash) { throw "Broken previous hash at $($record.id)." }
        $canonical = Get-Canonical -Record $record
        $calculated = Get-Hash -Text $canonical
        if ($calculated -ne $record.record_sha256) { throw "Bad record hash at $($record.id)." }
        $priorHash = $calculated
    }

    if ($ids.Contains($Id)) { throw "Duplicate ID: $Id" }
    foreach ($supersededId in $Supersedes) {
        if (-not $ids.Contains($supersededId)) {
            throw "Superseded ID is not already present: $supersededId"
        }
    }

    $newRecord = [pscustomobject]@{
        id                 = $Id
        time_utc           = $TimeUtc
        kind               = $Kind
        decision           = $Decision
        rationale          = $Rationale
        evidence           = @($Evidence)
        supersedes         = @($Supersedes)
        prev_record_sha256 = $priorHash
    }
    $canonical = Get-Canonical -Record $newRecord
    $recordHash = Get-Hash -Text $canonical
    $output = [ordered]@{
        schema             = 'github-maint-log/v1'
        id                 = $Id
        time_utc           = $TimeUtc
        kind               = $Kind
        decision           = $Decision
        rationale          = $Rationale
        evidence           = @($Evidence)
        supersedes         = @($Supersedes)
        prev_record_sha256 = $priorHash
        record_sha256      = $recordHash
    }
    $line = (($output | ConvertTo-Json -Compress -Depth 6).Replace("`r`n", "`n")) + "`n"
    $lineBytes = $utf8.GetBytes($line)
    [void]$stream.Seek(0, [IO.SeekOrigin]::End)
    $stream.Write($lineBytes, 0, $lineBytes.Length)
    $stream.Flush($true)

    [pscustomobject]@{
        path          = $LogPath.Replace('\', '/')
        records       = $lines.Count + 1
        appended_id   = $Id
        record_sha256 = $recordHash
    } | ConvertTo-Json -Compress
}
finally {
    $stream.Dispose()
}
