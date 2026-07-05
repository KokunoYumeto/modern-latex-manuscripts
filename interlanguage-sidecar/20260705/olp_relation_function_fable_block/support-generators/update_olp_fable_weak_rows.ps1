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

function Guess-Language {
  param([Parameter(Mandatory = $true)][string]$RelativePath)
  if ($RelativePath -like '*macedonian*') { return 'mk' }
  if ($RelativePath -like '*belarusian*') { return 'be' }
  if ($RelativePath -like '*sorbian*') { return 'hsb' }
  if ($RelativePath -like '*openlogic*' -or $RelativePath -like '*dmoi*' -or $RelativePath -like '*openintro*' -or $RelativePath -like '*aata*') { return 'en' }
  return 'und'
}

function Guess-Branch {
  param([Parameter(Mandatory = $true)][string]$Language)
  switch ($Language) {
    'mk' { 'Slavic/South' }
    'be' { 'Slavic/East' }
    'hsb' { 'Slavic/West' }
    'en' { 'Germanic/West Germanic' }
    default { 'undetermined' }
  }
}

function Normalize-Context {
  param([string]$Text)
  $clean = ($Text -replace '\s+', ' ').Trim()
  if ($clean.Length -gt 700) { return $clean.Substring(0, 700) }
  return $clean
}

$terms = @(
  @{
    lexeme_id = 'rf_codomain'
    probe_label = 'codomain_weak_row'
    pattern = '(?i)(codomain|co-domain|kodomen|kodomenot|codominio)'
    form_hint = 'codomain/kodomen'
  },
  @{
    lexeme_id = 'rf_composition'
    probe_label = 'composition_weak_row'
    pattern = '(?i)(composition|compose|composite|composit|kompozic|sostav|slozen|slozhen)'
    form_hint = 'composition/sostav/kompozicija'
  },
  @{
    lexeme_id = 'rf_inverse'
    probe_label = 'inverse_weak_row'
    pattern = '(?i)(inverse|invers|inverz|obratn|reciprocal)'
    form_hint = 'inverse/inverzna/obratna'
  }
)

$sourceRoot = Join-Path $ResolvedRoot 'source_bodies'
$files = Get-ChildItem -LiteralPath $sourceRoot -Recurse -File |
  Where-Object { $_.Extension.ToLowerInvariant() -in @('.txt', '.html', '.tex', '.ptx', '.qmd') } |
  Sort-Object FullName

$countRows = New-Object System.Collections.Generic.List[object]
$windowRows = New-Object System.Collections.Generic.List[object]

foreach ($file in $files) {
  $rel = RelPath $file.FullName
  $lang = Guess-Language $rel
  $branch = Guess-Branch $lang
  $lines = Get-Content -LiteralPath $file.FullName -ErrorAction Stop

  foreach ($term in $terms) {
    $termMatches = New-Object System.Collections.Generic.List[object]
    for ($i = 0; $i -lt $lines.Count; $i++) {
      $line = [string]$lines[$i]
      if ($line -match $term.pattern) {
        $termMatches.Add([pscustomobject]@{
          line_number = ($i + 1)
          line = (Normalize-Context $line)
        }) | Out-Null
      }
    }

    if ($termMatches.Count -gt 0) {
      $countRows.Add([pscustomobject]@{
        lexeme_id = $term.lexeme_id
        probe_label = $term.probe_label
        language = $lang
        branch = $branch
        source_path = $rel
        hit_count = $termMatches.Count
        source_use_status = 'weak-row source probe; not native review; not accepted terminology'
      }) | Out-Null

      foreach ($match in ($termMatches | Select-Object -First 12)) {
        $start = [Math]::Max(0, $match.line_number - 3)
        $end = [Math]::Min($lines.Count - 1, $match.line_number + 1)
        $context = Normalize-Context (($start..$end | ForEach-Object { [string]$lines[$_] }) -join ' ')
        $windowRows.Add([pscustomobject]@{
          lexeme_id = $term.lexeme_id
          probe_label = $term.probe_label
          language = $lang
          branch = $branch
          source_path = $rel
          line_number = $match.line_number
          matched_line = $match.line
          context_window = $context
          source_use_status = 'weak-row source-probe context; verify before translation use'
        }) | Out-Null
      }
    }
  }
}

Export-CsvRows 'weak_row_probe_counts.csv' $countRows
$jsonl = foreach ($row in $windowRows) { $row | ConvertTo-Json -Compress }
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'weak_row_probe_context_windows.jsonl') -Value $jsonl -Encoding utf8

$candidateRows = @(
  [pscustomobject]@{
    lexeme_id = 'rf_codomain'
    language = 'mk'
    branch = 'Slavic/South'
    script = 'Latin transliteration in source text'
    source_form = 'kodomen'
    normalized_form = 'kodomen'
    source_document = 'src-fable-recovery-mk-lexicon'
    source_location = 'macedonian_ukim_math_lexicon.txt lines 49077, 49090, 66978; weak_row_probe_context_windows.jsonl'
    witness_category = 'source-witness; weak-row term-probe; not native review'
  },
  [pscustomobject]@{
    lexeme_id = 'rf_composition'
    language = 'mk'
    branch = 'Slavic/South'
    script = 'Latin transliteration in source text'
    source_form = 'sostav / kompozicija'
    normalized_form = 'sostav-kompozicija'
    source_document = 'src-fable-recovery-mk-lexicon'
    source_location = 'macedonian_ukim_math_lexicon.txt lines 11513 and 18751; composition of mappings/functions context'
    witness_category = 'source-witness; weak-row term-probe; not native review'
  },
  [pscustomobject]@{
    lexeme_id = 'rf_inverse'
    language = 'mk'
    branch = 'Slavic/South'
    script = 'Latin transliteration in source text'
    source_form = 'inverzna funkcija / obratna'
    normalized_form = 'inverzna-obratna'
    source_document = 'src-fable-recovery-mk-lexicon'
    source_location = 'macedonian_ukim_math_lexicon.txt lines 3350, 3405, 3447; inverse-function contexts, not inverse-image approval'
    witness_category = 'source-witness; weak-row term-probe; not native review'
  },
  [pscustomobject]@{
    lexeme_id = 'rf_composition'
    language = 'hsb'
    branch = 'Slavic/West'
    script = 'Latin-script source text'
    source_form = 'kompozicije'
    normalized_form = 'kompozicije'
    source_document = 'src-fable-recovery-hsb-terminology'
    source_location = 'sorbian_domowina_math_terminology_2008.txt lines 4460, 4486, 6183; general composition witness with weak mathematical-topic fit'
    witness_category = 'source-witness; weak-row general-terminology probe; weak topic fit; not native review'
  }
)

Export-CsvRows 'weak_row_recovered_form_candidates.csv' $candidateRows

$statusRows = foreach ($term in $terms) {
  $termCounts = @($countRows | Where-Object { $_.lexeme_id -eq $term.lexeme_id })
  $branches = @($termCounts | Where-Object { $_.hit_count -gt 0 } | Select-Object -ExpandProperty branch -Unique)
  $forms = @($candidateRows | Where-Object { $_.lexeme_id -eq $term.lexeme_id })
  [pscustomobject]@{
    lexeme_id = $term.lexeme_id
    searched_patterns = $term.pattern
    source_files_searched = $files.Count
    probe_hit_rows = $termCounts.Count
    hit_branches = ($branches -join '; ')
    recovered_form_candidates = (($forms | ForEach-Object { "$($_.language):$($_.normalized_form)" }) -join '; ')
    recovery_status = if ($forms.Count -gt 0) { 'candidate-source-probe-recorded' } else { 'source-acquisition-gap' }
    next_action = 'language owner must source-check context, formula-neighboring usage, and false-friend risk before any rendering use'
    claim_boundary = 'generated-draft/source-probe only; no native review, no accepted terminology, no approval'
  }
}
Export-CsvRows 'weak_row_recovery_status.csv' $statusRows

$formsPath = Join-Path $ResolvedRoot 'forms.csv'
$forms = @(Import-Csv -LiteralPath $formsPath) | Where-Object { $_.witness_category -notlike '*weak-row*' }
($forms + $candidateRows) | Export-Csv -LiteralPath $formsPath -NoTypeInformation -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'rules_acknowledgement.md') -Value "`n## Weak-Row Recovery Addendum`n`nAdded `weak_row_probe_counts.csv`, `weak_row_probe_context_windows.jsonl`, `weak_row_recovered_form_candidates.csv`, and `weak_row_recovery_status.csv` for rf_codomain, rf_composition, and rf_inverse. Candidate forms were appended to `forms.csv` as source probes only. They are not reviewer returns, native review, accepted terminology, approval, or translation completion."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'FABLE_REQUIREMENTS_ACKNOWLEDGED_20260705.md') -Value "`n## Weak-Row Recovery Addendum`n`nWeak Germanic-only relation/function rows now have explicit source-probe recovery artifacts. Macedonian codomain/composition/inverse evidence and a weak Upper Sorbian general composition witness are recorded with branch labels and caveats. These satisfy audit visibility, not term promotion."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nWeak-row recovery addendum: generated weak_row_probe_counts.csv, weak_row_probe_context_windows.jsonl, weak_row_recovered_form_candidates.csv, and weak_row_recovery_status.csv; appended weak-row source-probe candidates to forms.csv without review or approval claims."

"WEAK_ROW_PROBE_COUNT_ROWS $($countRows.Count)"
"WEAK_ROW_CONTEXT_ROWS $($windowRows.Count)"
"WEAK_ROW_FORM_CANDIDATES $($candidateRows.Count)"
