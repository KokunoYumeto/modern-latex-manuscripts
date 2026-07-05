$ErrorActionPreference = 'Stop'

$Root = 'C:\Users\memo_\Documents\Codex\2026-07-04\noether-olp-relation-function-support\interlanguage-sidecar\20260705\olp_relation_function_fable_block'
$ResolvedRoot = [System.IO.Path]::GetFullPath($Root)
if (!(Test-Path -LiteralPath $ResolvedRoot)) {
  throw "Missing Fable block root: $ResolvedRoot"
}

function RelPath {
  param([Parameter(Mandatory = $true)][string]$Path)
  return ([System.IO.Path]::GetFullPath($Path).Substring($ResolvedRoot.Length).TrimStart('\') -replace '\\', '/')
}

function Ensure-Dir {
  param([Parameter(Mandatory = $true)][string]$Path)
  if (!(Test-Path -LiteralPath $Path)) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
  }
}

function Export-CsvRows {
  param(
    [Parameter(Mandatory = $true)][string]$RelativePath,
    [Parameter(Mandatory = $true)]$Rows
  )
  $Path = Join-Path $ResolvedRoot $RelativePath
  Ensure-Dir ([System.IO.Path]::GetDirectoryName($Path))
  $items = @()
  foreach ($row in $Rows) { $items += $row }
  $items | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding utf8
}

function Pattern-For {
  param([string]$LexemeId)
  switch ($LexemeId) {
    'rf_relation' { '(?i)(relation|relac|adnos|odnos)' }
    'rf_function' { '(?i)(function|funkc|funkcy|funkts)' }
    'rf_domain' { '(?i)(domain|domen)' }
    'rf_codomain' { '(?i)(codomain|kodomen|target set)' }
    'rf_image_range' { '(?i)(image|range|obraz|wobraz|opseg)' }
    'rf_injective' { '(?i)(inject|injekt|one-to-one|ednoznach)' }
    'rf_surjective' { '(?i)(surject|surjekt|onto)' }
    'rf_bijective' { '(?i)(biject|bijekt|biekc|one-to-one correspondence)' }
    'rf_equivalence_relation' { '(?i)(equiv|ekviv|equivalence)' }
    'rf_partial_order' { '(?i)(partial order|order|porad|parc)' }
    'rf_composition' { '(?i)(composition|compose|composit|kompozic|sostav)' }
    'rf_inverse' { '(?i)(inverse|invers|inverz|obratn|reciprocal)' }
    'rf_cardinality' { '(?i)(cardinal|kardinal)' }
    'rf_linear_map' { '(?i)(linear|linearn|homomorf)' }
    default { '(?i)(relation|function|mapping)' }
  }
}

function Branch-For-Path {
  param([string]$Rel)
  if ($Rel -like '*belarusian*') { return 'Slavic_East' }
  if ($Rel -like '*sorbian*') { return 'Slavic_West' }
  return 'Other'
}

function Normalize-Context {
  param([string]$Text)
  $clean = ($Text -replace '\s+', ' ').Trim()
  if ($clean.Length -gt 700) { return $clean.Substring(0, 700) }
  return $clean
}

function Classify-Hit {
  param(
    [string]$Rel,
    [string]$LexemeId,
    [string]$Line
  )
  if ($Rel -like '*.html' -and $Line -match '(?i)(<script|function\(|favicon|og:image|product-main-image|iframe|analytics|mixpanel|data-full|src=|href=)') {
    return 'page-runtime-or-product-noise'
  }
  if ($LexemeId -eq 'rf_image_range' -and $Rel -like '*sorbian*' -and $Line -match '(?i)(wobrazki|wobrazy|image einer|product|kniha|bibli|antologija)') {
    return 'general-image-language-noise'
  }
  if ($Rel -like '*sorbian*' -and $Line -match '(?i)(kompozicije|wobraz|zwjazk)' ) {
    return 'general-terminology-or-language-context'
  }
  return 'candidate-source-context-needs-human-check'
}

$queuePath = Join-Path $ResolvedRoot 'branch_gap_recovery_queue.csv'
if (!(Test-Path -LiteralPath $queuePath)) {
  throw 'Run update_olp_fable_gap_queue.ps1 before East/West gap audit.'
}

$queue = @(Import-Csv -LiteralPath $queuePath)
$sourceRoot = Join-Path $ResolvedRoot 'source_bodies\fable_mirror_underrepresented_slavic'
$files = Get-ChildItem -LiteralPath $sourceRoot -Recurse -File |
  Where-Object { $_.Extension.ToLowerInvariant() -in @('.txt', '.html') } |
  Sort-Object FullName

$auditRows = New-Object System.Collections.Generic.List[object]
$contextRows = New-Object System.Collections.Generic.List[object]

foreach ($row in $queue) {
  $missing = @($row.missing_active_branches -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -in @('Slavic_East', 'Slavic_West') })
  if ($missing.Count -eq 0) { continue }
  $pattern = Pattern-For $row.lexeme_id
  foreach ($branch in $missing) {
    $branchFiles = @($files | Where-Object { Branch-For-Path (RelPath $_.FullName) -eq $branch })
    $rawHits = 0
    $candidateHits = 0
    $noiseHits = 0
    foreach ($file in $branchFiles) {
      $rel = RelPath $file.FullName
      $lines = Get-Content -LiteralPath $file.FullName -ErrorAction Stop
      for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = [string]$lines[$i]
        if ($line -match $pattern) {
          $rawHits += 1
          $class = Classify-Hit $rel $row.lexeme_id $line
          if ($class -eq 'candidate-source-context-needs-human-check') { $candidateHits += 1 } else { $noiseHits += 1 }
          if ($contextRows.Count -lt 240) {
            $start = [Math]::Max(0, $i - 2)
            $end = [Math]::Min($lines.Count - 1, $i + 2)
            $context = Normalize-Context (($start..$end | ForEach-Object { [string]$lines[$_] }) -join ' ')
            $contextRows.Add([pscustomobject]@{
              lexeme_id = $row.lexeme_id
              missing_branch = $branch
              source_path = $rel
              line_number = ($i + 1)
              classification = $class
              matched_line = Normalize-Context $line
              context_window = $context
              source_use_status = 'gap-audit probe only; not counted as term evidence without owner/source check'
            }) | Out-Null
          }
        }
      }
    }
    $status = if ($candidateHits -gt 0) {
      'candidate-hit-needs-source-check-not-counted'
    } elseif ($rawHits -gt 0) {
      'only-noise-or-general-page-hit'
    } else {
      'no-in-package-hit'
    }
    $auditRows.Add([pscustomobject]@{
      lexeme_id = $row.lexeme_id
      missing_branch = $branch
      searched_files = $branchFiles.Count
      regex = $pattern
      raw_hit_count = $rawHits
      candidate_context_count = $candidateHits
      noise_or_general_count = $noiseHits
      audit_status = $status
      next_action = 'recover cleaner source body or owner-verified context before using as positive branch witness'
      claim_boundary = 'gap audit only; no native review, no accepted terminology, no source certification'
    }) | Out-Null
  }
}

Export-CsvRows 'east_west_gap_probe_audit.csv' $auditRows
$jsonl = foreach ($item in $contextRows) { $item | ConvertTo-Json -Compress }
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'east_west_gap_probe_contexts.jsonl') -Value $jsonl -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nEast/West gap audit addendum: generated east_west_gap_probe_audit.csv and east_west_gap_probe_contexts.jsonl by probing in-package Belarusian and Upper Sorbian bodies for missing East/West branches. Runtime/page noise and general-language hits are separated from candidate source contexts and are not counted as positive term evidence."

# Rebuild manifest excluding itself and SHA; SHA includes manifest.
$manifestPath = Join-Path $ResolvedRoot 'MANIFEST.csv'
$sumPath = Join-Path $ResolvedRoot 'SHA256SUMS.txt'
$manifestRows = Get-ChildItem -LiteralPath $ResolvedRoot -Recurse -File |
  Where-Object { $_.FullName -notin @($manifestPath, $sumPath) } |
  Sort-Object FullName |
  ForEach-Object {
    $rel = RelPath $_.FullName
    $top = ($rel -split '/')[0]
    $label = switch ($top) {
      'source_bodies' { 'source-witness' }
      'source_witnesses' { 'source-witness' }
      'generated-draft' { 'generated-draft' }
      'support-generators' { 'support-generator' }
      default {
        if ($rel -match 'ledger|languages|source_documents|forms|weights|intelligibility|do_not_use|recovery|probe|candidate|measure|summary|scaffold|route|handoff|queue|audit|contexts|PRETRANSLATION|acknowledgement|ACKNOWLEDGED') { 'audit-ledger' } else { 'methodology' }
      }
    }
    [pscustomobject]@{
      relative_path = $rel
      bytes = $_.Length
      sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
      source_use_label = $label
      note = 'Fable OLP relation/function block; no approval or completion claim'
    }
  }
$manifestRows | Export-Csv -LiteralPath $manifestPath -NoTypeInformation -Encoding utf8

$sumLines = Get-ChildItem -LiteralPath $ResolvedRoot -Recurse -File |
  Where-Object { $_.FullName -ne $sumPath } |
  Sort-Object FullName |
  ForEach-Object {
    $rel = RelPath $_.FullName
    $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash.ToLowerInvariant()
    "$hash  $rel"
  }
Set-Content -LiteralPath $sumPath -Value $sumLines -Encoding ascii

"EAST_WEST_AUDIT_ROWS $($auditRows.Count)"
"EAST_WEST_CONTEXT_ROWS $($contextRows.Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath $manifestPath | Measure-Object).Count)"
