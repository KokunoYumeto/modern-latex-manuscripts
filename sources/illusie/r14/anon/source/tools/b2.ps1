param(
  [Parameter(Mandatory = $true)] [string]$ProjectRoot,
  [Parameter(Mandatory = $true)] [string]$Generation,
  [Parameter(Mandatory = $true)] [int]$Pages
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($Generation -notmatch '^p[0-9]+r[0-9]+$') { throw 'Invalid generation.' }
if ($Pages -lt 1) { throw 'Pages must be positive.' }

$root = [IO.Path]::GetFullPath($ProjectRoot)
$build = [IO.Path]::GetFullPath((Join-Path $root "builds\$Generation"))
$relative = [IO.Path]::GetRelativePath($root, $build)
if ([IO.Path]::IsPathRooted($relative) -or $relative -eq '..' -or $relative.StartsWith("..$([IO.Path]::DirectorySeparatorChar)")) {
  throw 'Build root escaped the project.'
}
if (Test-Path -LiteralPath $build) {
  if ((Get-ChildItem -LiteralPath $build -Force).Count -ne 0) { throw 'No overwrite.' }
} else {
  New-Item -ItemType Directory -Path $build | Out-Null
}

$lanes = [ordered]@{
  fr = 'readers\fr.tex'
  en = 'readers\en.tex'
}
$bad = @(
  'LaTeX Warning:', 'Package\s+\S+\s+Warning:', 'LaTeX Font Warning:',
  'Missing character:', 'Undefined control sequence', 'Emergency stop',
  'Fatal error', 'Overfull \\hbox', 'Underfull \\hbox', 'Rerun to get',
  'Size substitutions with differences', 'destination with the same identifier',
  'multiply defined'
)
$result = @()

Push-Location -LiteralPath $root
try {
  foreach ($lane in $lanes.Keys) {
    $dir = Join-Path $build $lane
    New-Item -ItemType Directory -Path $dir | Out-Null
    $latexArgs = @(
      '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
      "-output-directory=$dir", '-jobname=book', $lanes[$lane]
    )
    1..3 | ForEach-Object {
      $console = & lualatex @latexArgs 2>&1
      if ($LASTEXITCODE -ne 0) {
        throw "$lane pass $_ failed.`n$(($console | Select-Object -Last 40) -join [Environment]::NewLine)"
      }
    }
    $pdf = Join-Path $dir 'book.pdf'
    $log = Join-Path $dir 'book.log'
    if (-not (Test-Path -LiteralPath $pdf) -or -not (Test-Path -LiteralPath $log)) { throw "$lane output missing." }
    $logText = Get-Content -Raw -LiteralPath $log
    $findings = @($bad | Where-Object { $logText -match $_ })
    if ($findings.Count -ne 0) { throw "$lane log findings: $($findings -join ', ')" }
    $bytes = (Get-Item -LiteralPath $pdf).Length
    if ($logText -notmatch "Output written on book\.pdf \($Pages pages, $bytes bytes\)\.") { throw "$lane page/byte mismatch." }
    $result += [ordered]@{
      generation = $Generation
      lane = $lane
      master = $lanes[$lane].Replace('\', '/')
      pages = $Pages
      pdf = ([IO.Path]::GetRelativePath($root, $pdf)).Replace('\', '/')
      bytes = $bytes
      sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $pdf).Hash
      log_findings = @()
    }
  }
} finally {
  Pop-Location
}
$result | ConvertTo-Json -Depth 4
