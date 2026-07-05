param(
  [string]$OutputPath = "github_hexwell_university_notes_main.zip"
)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifest = Join-Path $root 'OVERSIZE_BODY_SPLIT_MANIFEST_20260706.csv'
$rows = Import-Csv -LiteralPath $manifest | Sort-Object part_number
$out = [System.IO.File]::Create((Join-Path $root $OutputPath))
try {
  foreach($row in $rows){
    $part = Join-Path $root ($row.part_path -replace '/', [System.IO.Path]::DirectorySeparatorChar)
    $in = [System.IO.File]::OpenRead($part)
    try { $in.CopyTo($out) } finally { $in.Dispose() }
  }
} finally { $out.Dispose() }
$hash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $root $OutputPath)).Hash.ToUpperInvariant()
$expected = ($rows | Select-Object -First 1).original_sha256.ToUpperInvariant()
if($hash -ne $expected){ throw "Reassembled SHA256 mismatch: $hash expected $expected" }
Write-Output "Reassembled $OutputPath with SHA256 $hash"
