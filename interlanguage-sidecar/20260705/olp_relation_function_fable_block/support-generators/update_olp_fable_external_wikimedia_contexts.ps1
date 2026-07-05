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

function Resolve-Rel {
  param([Parameter(Mandatory = $true)][string]$Rel)
  return Join-Path $ResolvedRoot ($Rel -replace '/', '\')
}

function Normalize-Context {
  param([string]$Text)
  $clean = ($Text -replace '\s+', ' ').Trim()
  if ($clean.Length -gt 900) { return $clean.Substring(0, 900) }
  return $clean
}

function Context-Window {
  param(
    [string[]]$Lines,
    [int]$Index
  )
  $start = [Math]::Max(0, $Index - 1)
  $end = [Math]::Min($Lines.Count - 1, $Index + 1)
  return Normalize-Context (($start..$end | ForEach-Object { [string]$Lines[$_] }) -join ' ')
}

$recoveryPath = Join-Path $ResolvedRoot 'external_wikimedia_source_recovery.csv'
if (!(Test-Path -LiteralPath $recoveryPath)) {
  throw 'Run update_olp_fable_external_wikimedia_recovery.ps1 before context extraction.'
}

$docs = @(Import-Csv -LiteralPath $recoveryPath)
$countRows = New-Object System.Collections.Generic.List[object]
$contextRows = New-Object System.Collections.Generic.List[object]

foreach ($doc in $docs) {
  $path = Resolve-Rel $doc.recovered_path
  if (!(Test-Path -LiteralPath $path)) {
    $countRows.Add([pscustomobject]@{
      doc_id = $doc.doc_id
      language = $doc.language
      branch = $doc.branch
      lexeme_ids = $doc.lexeme_ids
      source_path = $doc.recovered_path
      line_count = 0
      lead_contexts = 0
      formula_contexts = 0
      emitted_contexts = 0
      status = 'source body missing at context-extraction time'
    }) | Out-Null
    continue
  }

  $lines = @(Get-Content -LiteralPath $path -ErrorAction Stop)
  $leadIndexes = New-Object System.Collections.Generic.List[int]
  for ($i = 0; $i -lt $lines.Count -and $leadIndexes.Count -lt 6; $i++) {
    if (([string]$lines[$i]).Trim() -ne '') { $leadIndexes.Add($i) | Out-Null }
  }

  $formulaIndexes = New-Object System.Collections.Generic.List[int]
  for ($i = 0; $i -lt $lines.Count -and $formulaIndexes.Count -lt 10; $i++) {
    $line = [string]$lines[$i]
    if ($line -match '<math|\\[A-Za-z]+|=\s|\\to|\\mapsto|\\frac|\\in|\\forall|\\exists') {
      $formulaIndexes.Add($i) | Out-Null
    }
  }

  $emitted = 0
  foreach ($i in $leadIndexes) {
    $contextRows.Add([pscustomobject]@{
      doc_id = $doc.doc_id
      lexeme_ids = $doc.lexeme_ids
      language = $doc.language
      branch = $doc.branch
      source_path = $doc.recovered_path
      source_url = $doc.source_url
      line_number = ($i + 1)
      context_type = 'lead-definition-or-opening-context'
      context_window = Context-Window $lines $i
      source_use_status = 'external source-canon candidate context; not counted as branch evidence'
    }) | Out-Null
    $emitted += 1
  }
  foreach ($i in $formulaIndexes) {
    $contextRows.Add([pscustomobject]@{
      doc_id = $doc.doc_id
      lexeme_ids = $doc.lexeme_ids
      language = $doc.language
      branch = $doc.branch
      source_path = $doc.recovered_path
      source_url = $doc.source_url
      line_number = ($i + 1)
      context_type = 'formula-or-symbol-neighboring-context'
      context_window = Context-Window $lines $i
      source_use_status = 'external source-canon candidate context; formula-neighboring check required before use'
    }) | Out-Null
    $emitted += 1
  }

  $countRows.Add([pscustomobject]@{
    doc_id = $doc.doc_id
    language = $doc.language
    branch = $doc.branch
    lexeme_ids = $doc.lexeme_ids
    source_path = $doc.recovered_path
    line_count = $lines.Count
    lead_contexts = $leadIndexes.Count
    formula_contexts = $formulaIndexes.Count
    emitted_contexts = $emitted
    status = 'context windows extracted; not branch-weight evidence'
  }) | Out-Null
}

$countRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'external_wikimedia_context_counts.csv') -NoTypeInformation -Encoding utf8
$jsonl = foreach ($row in $contextRows) { $row | ConvertTo-Json -Compress }
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'external_wikimedia_context_windows.jsonl') -Value $jsonl -Encoding utf8

$summaryRows = @(
  [pscustomobject]@{ field='source_bodies_scanned'; value=$docs.Count; note='Rows from external_wikimedia_source_recovery.csv' },
  [pscustomobject]@{ field='context_windows_emitted'; value=$contextRows.Count; note='Lead and formula-neighboring windows; candidate support only' },
  [pscustomobject]@{ field='branch_weight_effect'; value='none'; note='No changes to forms.csv, term_probe_counts.csv, or branch_weight_ledger.csv' }
)
$summaryRows | Export-Csv -LiteralPath (Join-Path $ResolvedRoot 'external_wikimedia_context_summary.csv') -NoTypeInformation -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nExternal Wikimedia context addendum: generated external_wikimedia_context_counts.csv, external_wikimedia_context_windows.jsonl, and external_wikimedia_context_summary.csv from recovered Polish/Ukrainian wikitext bodies. Context windows are source-canon candidate support only and do not alter forms or branch weights."

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
        if ($rel -match 'ledger|languages|source_documents|forms|weights|intelligibility|do_not_use|recovery|probe|candidate|blocker|measure|summary|scaffold|route|handoff|queue|audit|contexts|context|PRETRANSLATION|acknowledgement|ACKNOWLEDGED|B3_PACKAGE') { 'audit-ledger' } else { 'methodology' }
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

"EXTERNAL_CONTEXT_DOCS $($docs.Count)"
"EXTERNAL_CONTEXT_WINDOWS $($contextRows.Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath $manifestPath | Measure-Object).Count)"
