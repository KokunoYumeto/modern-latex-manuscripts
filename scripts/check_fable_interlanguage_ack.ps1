param(
  [string]$Repo
)

if (-not $Repo) {
  $Repo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
}

$required = @(
  'weighted rooted-tree witness measure',
  'branch-weight witness ledger',
  'marginal intelligibility',
  'per-language source index',
  'per-word/per-concept interlanguage index',
  'dominance-collapse',
  'source-use ledger',
  'whole corpus as-is'
)

$acks = Get-ChildItem -LiteralPath $Repo -Recurse -File -Filter 'FABLE_REQUIREMENTS_ACKNOWLEDGED_*.md' -ErrorAction SilentlyContinue
if (-not $acks) {
  Write-Output 'MISSING: no FABLE_REQUIREMENTS_ACKNOWLEDGED_YYYYMMDD.md file found.'
  exit 2
}

$joined = ($acks | ForEach-Object { Get-Content -Raw -LiteralPath $_.FullName }) -join "`n"
$missing = @()
foreach ($term in $required) {
  if ($joined -notmatch [regex]::Escape($term)) { $missing += $term }
}

if ($missing.Count -gt 0) {
  Write-Output 'INCOMPLETE: acknowledgement exists but does not name all required rules.'
  $missing | ForEach-Object { Write-Output "MISSING_TERM: $_" }
  exit 3
}

Write-Output 'OK: Fable acknowledgement found and names all required rule groups.'
exit 0
