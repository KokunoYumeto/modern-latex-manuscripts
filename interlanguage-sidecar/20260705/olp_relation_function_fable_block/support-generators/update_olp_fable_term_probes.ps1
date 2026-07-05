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
  $Rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding utf8
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

$terms = @(
  @{ lexeme_id='rf_function'; label='function'; pattern='(?i)(function|funkcij|funkcii|funkcija|funkcije)' },
  @{ lexeme_id='rf_relation'; label='relation'; pattern='(?i)(relation|relacij|relacija|odnos)' },
  @{ lexeme_id='rf_domain'; label='domain'; pattern='(?i)(domain|domen|domain of a map|domain of a function)' },
  @{ lexeme_id='rf_image_range'; label='image_range'; pattern='(?i)(image|range|obraz|slika)' },
  @{ lexeme_id='rf_injective'; label='injective'; pattern='(?i)(inject|injektiv)' },
  @{ lexeme_id='rf_surjective'; label='surjective'; pattern='(?i)(surject|surjektiv)' },
  @{ lexeme_id='rf_bijective'; label='bijective'; pattern='(?i)(biject|biektiv|bijection)' },
  @{ lexeme_id='rf_equivalence_relation'; label='equivalence'; pattern='(?i)(equiv|ekviv|ekvivalen)' },
  @{ lexeme_id='rf_partial_order'; label='partial_order'; pattern='(?i)(partial order|parcijalen.*red|order)' },
  @{ lexeme_id='rf_cardinality'; label='cardinality'; pattern='(?i)(cardinal|kardinal)' },
  @{ lexeme_id='rf_linear_map'; label='linear_map_homomorphism'; pattern='(?i)(linear|linearn|homomorph|homomorf)' }
)

$sourceRoot = Join-Path $ResolvedRoot 'source_bodies'
$files = Get-ChildItem -LiteralPath $sourceRoot -Recurse -File |
  Where-Object { $_.Extension.ToLowerInvariant() -in @('.txt', '.html', '.tex', '.ptx', '.qmd') } |
  Sort-Object FullName

$countRows = New-Object System.Collections.Generic.List[object]
$windowRows = New-Object System.Collections.Generic.List[object]
$formsProbeRows = New-Object System.Collections.Generic.List[object]

foreach ($file in $files) {
  $rel = RelPath $file.FullName
  $lang = Guess-Language $rel
  $branch = Guess-Branch $lang
  $lines = Get-Content -LiteralPath $file.FullName -ErrorAction Stop

  foreach ($term in $terms) {
    $termMatches = @()
    for ($i = 0; $i -lt $lines.Count; $i++) {
      $line = [string]$lines[$i]
      if ($line -match $term.pattern) {
        $matchObject = [pscustomobject]@{ line_number = ($i + 1); line = ($line.Trim() -replace '\s+', ' ') }
        $termMatches += $matchObject
      }
    }

    if ($termMatches.Count -gt 0) {
      $countRows.Add([pscustomobject]@{
        lexeme_id = $term.lexeme_id
        probe_label = $term.label
        language = $lang
        branch = $branch
        source_path = $rel
        hit_count = $termMatches.Count
        source_use_status = 'term-probe; not native review; not accepted terminology'
      }) | Out-Null

      foreach ($match in ($termMatches | Select-Object -First 8)) {
        $start = [Math]::Max(0, $match.line_number - 2)
        $end = [Math]::Min($lines.Count - 1, $match.line_number)
        $context = (($start..$end | ForEach-Object { ([string]$lines[$_]).Trim() }) -join ' ' -replace '\s+', ' ')
        if ($context.Length -gt 500) { $context = $context.Substring(0, 500) }
        $windowRows.Add([pscustomobject]@{
          lexeme_id = $term.lexeme_id
          probe_label = $term.label
          language = $lang
          branch = $branch
          source_path = $rel
          line_number = $match.line_number
          matched_line = $match.line
          context_window = $context
          source_use_status = 'term-probe context; verify before forms promotion'
        }) | Out-Null
      }
    }
  }
}

Export-CsvRows 'term_probe_counts.csv' $countRows
$jsonl = foreach ($row in $windowRows) { $row | ConvertTo-Json -Compress }
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'term_probe_context_windows.jsonl') -Value $jsonl -Encoding utf8

# Cautious explicit form probes from the Macedonian lexicon only. These are source-body term probes, not approval.
$explicitForms = @(
  [pscustomobject]@{ lexeme_id='rf_function'; language='mk'; branch='Slavic/South'; script='Latin transliteration in source text'; source_form='funkcija'; normalized_form='funkcija'; source_document='src-fable-recovery-mk-lexicon'; source_location='macedonian_ukim_math_lexicon.txt lines with function/funkcija'; witness_category='source-witness; term-probe; not native review' },
  [pscustomobject]@{ lexeme_id='rf_relation'; language='mk'; branch='Slavic/South'; script='Latin transliteration in source text'; source_form='relacija'; normalized_form='relacija'; source_document='src-fable-recovery-mk-lexicon'; source_location='macedonian_ukim_math_lexicon.txt lines with relation/relacija'; witness_category='source-witness; term-probe; not native review' },
  [pscustomobject]@{ lexeme_id='rf_domain'; language='mk'; branch='Slavic/South'; script='Latin transliteration in source text'; source_form='domen'; normalized_form='domen'; source_document='src-fable-recovery-mk-lexicon'; source_location='macedonian_ukim_math_lexicon.txt line with Funkcija f so domen D'; witness_category='source-witness; term-probe; not native review' },
  [pscustomobject]@{ lexeme_id='rf_bijective'; language='mk'; branch='Slavic/South'; script='mixed source line'; source_form='biektivno/bijective mapping probe'; normalized_form='biektivno'; source_document='src-fable-recovery-mk-lexicon'; source_location='macedonian_ukim_math_lexicon.txt line with bijective mapping'; witness_category='source-witness; term-probe; not native review' },
  [pscustomobject]@{ lexeme_id='rf_cardinality'; language='mk'; branch='Slavic/South'; script='Latin transliteration in source text'; source_form='kardinalen/kardinalno probe'; normalized_form='kardinal'; source_document='src-fable-recovery-mk-lexicon'; source_location='macedonian_ukim_math_lexicon.txt line with cardinal number'; witness_category='source-witness; term-probe; not native review' }
)
Export-CsvRows 'recovered_source_form_candidates.csv' $explicitForms

$formsPath = Join-Path $ResolvedRoot 'forms.csv'
$forms = @(Import-Csv -LiteralPath $formsPath) | Where-Object { $_.witness_category -notlike '*term-probe*' }
($forms + $explicitForms) | Export-Csv -LiteralPath $formsPath -NoTypeInformation -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'rules_acknowledgement.md') -Value "`n## Term-Probe Addendum`n`nAdded `term_probe_counts.csv`, `term_probe_context_windows.jsonl`, and `recovered_source_form_candidates.csv`. Macedonian source-form candidates were appended to `forms.csv` as `source-witness; term-probe; not native review`. No candidate is promoted to accepted terminology."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'FABLE_REQUIREMENTS_ACKNOWLEDGED_20260705.md') -Value "`n## Term-Probe Addendum`n`nThe package now includes term-probe counts and capped context windows over copied source bodies. Explicit Macedonian relation/function candidates are recorded as term probes only, not reviewer return, native review, accepted terminology, or translation completion."
Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nTerm-probe addendum: generated term_probe_counts.csv, term_probe_context_windows.jsonl, recovered_source_form_candidates.csv, and appended term-probe rows to forms.csv with non-review caveats."

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
      default {
        if ($rel -match 'ledger|languages|source_documents|forms|weights|intelligibility|do_not_use|recovery|probe|acknowledgement|ACKNOWLEDGED') { 'audit-ledger' } else { 'methodology' }
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

"TERM_PROBE_COUNT_ROWS $($countRows.Count)"
"TERM_PROBE_CONTEXT_ROWS $($windowRows.Count)"
"RECOVERED_FORM_CANDIDATES $($explicitForms.Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath $manifestPath | Measure-Object).Count)"
"FILES $((Get-ChildItem -LiteralPath $ResolvedRoot -Recurse -File | Measure-Object).Count)"
