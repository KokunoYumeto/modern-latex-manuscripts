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
  if ($items.Count -eq 0) {
    Set-Content -LiteralPath $Path -Value '' -Encoding utf8
  } else {
    $items | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding utf8
  }
}

function Invoke-RawPage {
  param(
    [Parameter(Mandatory = $true)][string]$Site,
    [Parameter(Mandatory = $true)][string]$EncodedTitle
  )
  $uri = "https://$($Site).wikipedia.org/w/index.php?title=$EncodedTitle&action=raw"
  return Invoke-WebRequest -UseBasicParsing -Uri $uri -Headers @{ 'User-Agent' = 'Noether OLP relation-function source-canon recovery (local research; package handoff)' } -TimeoutSec 45
}

$date = '20260705'
$bodyRoot = Join-Path $ResolvedRoot "source_bodies\external_wikimedia_recovery\$date"
$witnessRoot = Join-Path $ResolvedRoot "source_witnesses\external_wikimedia_recovery\$date"
Ensure-Dir $bodyRoot
Ensure-Dir $witnessRoot

$docs = @(
  @{ doc_id='src-ext-wikimedia-pl-injective'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Funkcja%20r%C3%B3%C5%BCnowarto%C5%9Bciowa'; page_url='https://pl.wikipedia.org/wiki/Funkcja_r%C3%B3%C5%BCnowarto%C5%9Bciowa'; file='pl_funkcja_roznicowartosciowa.wiki.txt'; lexeme_ids='rf_injective; rf_bijective' },
  @{ doc_id='src-ext-wikimedia-pl-surjective'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Surjekcja'; page_url='https://pl.wikipedia.org/wiki/Surjekcja'; file='pl_surjekcja.wiki.txt'; lexeme_ids='rf_surjective' },
  @{ doc_id='src-ext-wikimedia-pl-bijective'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Funkcja%20wzajemnie%20jednoznaczna'; page_url='https://pl.wikipedia.org/wiki/Funkcja_wzajemnie_jednoznaczna'; file='pl_funkcja_wzajemnie_jednoznaczna.wiki.txt'; lexeme_ids='rf_bijective; rf_inverse' },
  @{ doc_id='src-ext-wikimedia-pl-domain'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Dziedzina%20%28matematyka%29'; page_url='https://pl.wikipedia.org/wiki/Dziedzina_(matematyka)'; file='pl_dziedzina_matematyka.wiki.txt'; lexeme_ids='rf_domain' },
  @{ doc_id='src-ext-wikimedia-pl-codomain'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Przeciwdziedzina'; page_url='https://pl.wikipedia.org/wiki/Przeciwdziedzina'; file='pl_przeciwdziedzina.wiki.txt'; lexeme_ids='rf_codomain; rf_image_range' },
  @{ doc_id='src-ext-wikimedia-pl-inverse'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Funkcja%20odwrotna'; page_url='https://pl.wikipedia.org/wiki/Funkcja_odwrotna'; file='pl_funkcja_odwrotna.wiki.txt'; lexeme_ids='rf_inverse; rf_bijective' },
  @{ doc_id='src-ext-wikimedia-pl-cardinality'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Moc%20zbioru'; page_url='https://pl.wikipedia.org/wiki/Moc_zbioru'; file='pl_moc_zbioru.wiki.txt'; lexeme_ids='rf_cardinality; rf_bijective' },
  @{ doc_id='src-ext-wikimedia-pl-linear-map'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Przekszta%C5%82cenie%20liniowe'; page_url='https://pl.wikipedia.org/wiki/Przekszta%C5%82cenie_liniowe'; file='pl_przeksztalcenie_liniowe.wiki.txt'; lexeme_ids='rf_linear_map; rf_function' },
  @{ doc_id='src-ext-wikimedia-pl-image'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Obraz%20%28matematyka%29'; page_url='https://pl.wikipedia.org/wiki/Obraz_(matematyka)'; file='pl_obraz_matematyka.wiki.txt'; lexeme_ids='rf_image_range; rf_function' },
  @{ doc_id='src-ext-wikimedia-pl-function'; site='pl'; language='pl'; branch='Slavic/West'; encoded_title='Funkcja'; page_url='https://pl.wikipedia.org/wiki/Funkcja'; file='pl_funkcja.wiki.txt'; lexeme_ids='rf_function; rf_domain; rf_codomain; rf_image_range' },
  @{ doc_id='src-ext-wikimedia-uk-injective'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%86%D0%BD%27%D1%94%D0%BA%D1%86%D1%96%D1%8F_%28%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%29'; page_url='https://uk.wikipedia.org/wiki/%D0%86%D0%BD%27%D1%94%D0%BA%D1%86%D1%96%D1%8F_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)'; file='uk_injection_math.wiki.txt'; lexeme_ids='rf_injective; rf_function' },
  @{ doc_id='src-ext-wikimedia-uk-surjective'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%A1%D1%8E%D1%80%27%D1%94%D0%BA%D1%86%D1%96%D1%8F'; page_url='https://uk.wikipedia.org/wiki/%D0%A1%D1%8E%D1%80%27%D1%94%D0%BA%D1%86%D1%96%D1%8F'; file='uk_surjection.wiki.txt'; lexeme_ids='rf_surjective; rf_function' },
  @{ doc_id='src-ext-wikimedia-uk-bijective'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%91%D1%96%D1%94%D0%BA%D1%86%D1%96%D1%8F'; page_url='https://uk.wikipedia.org/wiki/%D0%91%D1%96%D1%94%D0%BA%D1%86%D1%96%D1%8F'; file='uk_bijection.wiki.txt'; lexeme_ids='rf_bijective; rf_inverse' },
  @{ doc_id='src-ext-wikimedia-uk-domain'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%20%D0%B2%D0%B8%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%BD%D1%8F'; page_url='https://uk.wikipedia.org/wiki/%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C_%D0%B2%D0%B8%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%BD%D1%8F'; file='uk_domain.wiki.txt'; lexeme_ids='rf_domain; rf_function' },
  @{ doc_id='src-ext-wikimedia-uk-function'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%8F%20%28%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%29'; page_url='https://uk.wikipedia.org/wiki/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%8F_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)'; file='uk_function_math.wiki.txt'; lexeme_ids='rf_function; rf_domain; rf_codomain; rf_image_range' },
  @{ doc_id='src-ext-wikimedia-uk-image-range'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D1%8C'; page_url='https://uk.wikipedia.org/wiki/%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C_%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D1%8C'; file='uk_image_range.wiki.txt'; lexeme_ids='rf_image_range; rf_function' },
  @{ doc_id='src-ext-wikimedia-uk-inverse'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%9E%D0%B1%D0%B5%D1%80%D0%BD%D0%B5%D0%BD%D0%B0%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%8F'; page_url='https://uk.wikipedia.org/wiki/%D0%9E%D0%B1%D0%B5%D1%80%D0%BD%D0%B5%D0%BD%D0%B0_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D1%96%D1%8F'; file='uk_inverse_function.wiki.txt'; lexeme_ids='rf_inverse; rf_bijective' },
  @{ doc_id='src-ext-wikimedia-uk-cardinality'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%9F%D0%BE%D1%82%D1%83%D0%B6%D0%BD%D1%96%D1%81%D1%82%D1%8C%20%D0%BC%D0%BD%D0%BE%D0%B6%D0%B8%D0%BD%D0%B8'; page_url='https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D1%82%D1%83%D0%B6%D0%BD%D1%96%D1%81%D1%82%D1%8C_%D0%BC%D0%BD%D0%BE%D0%B6%D0%B8%D0%BD%D0%B8'; file='uk_cardinality_set.wiki.txt'; lexeme_ids='rf_cardinality; rf_bijective' },
  @{ doc_id='src-ext-wikimedia-uk-linear-map'; site='uk'; language='uk'; branch='Slavic/East'; encoded_title='%D0%9B%D1%96%D0%BD%D1%96%D0%B9%D0%BD%D0%B5%20%D0%B2%D1%96%D0%B4%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F'; page_url='https://uk.wikipedia.org/wiki/%D0%9B%D1%96%D0%BD%D1%96%D0%B9%D0%BD%D0%B5_%D0%B2%D1%96%D0%B4%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%BD%D1%8F'; file='uk_linear_map.wiki.txt'; lexeme_ids='rf_linear_map; rf_function' }
)

$licenseRows = @(
  [pscustomobject]@{ project='plwiki'; raw_endpoint='https://pl.wikipedia.org/w/index.php?title={encoded_title}&action=raw'; rights_signal_url='https://creativecommons.org/licenses/by-sa/4.0/'; terms_url='https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use'; note='Wikimedia source export/access signal; no license-clearance claim' },
  [pscustomobject]@{ project='ukwiki'; raw_endpoint='https://uk.wikipedia.org/w/index.php?title={encoded_title}&action=raw'; rights_signal_url='https://creativecommons.org/licenses/by-sa/4.0/'; terms_url='https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use'; note='Wikimedia source export/access signal; no license-clearance claim' }
)
Export-CsvRows "source_witnesses/external_wikimedia_recovery/$date/wikimedia_access_license_signal.csv" $licenseRows

$recoveryRows = New-Object System.Collections.Generic.List[object]
$coverageRows = New-Object System.Collections.Generic.List[object]
$blockerRows = New-Object System.Collections.Generic.List[object]
$sourceDocRows = New-Object System.Collections.Generic.List[object]

foreach ($doc in $docs) {
  $phase = 'start'
  $bodyPath = Join-Path $bodyRoot $doc.file
  $relBody = RelPath $bodyPath
  $uri = "https://$($doc.site).wikipedia.org/w/index.php?title=$($doc.encoded_title)&action=raw"
  try {
    $phase = 'invoke-raw-page'
    $response = Invoke-RawPage -Site $doc.site -EncodedTitle $doc.encoded_title
    $phase = 'read-content'
    $content = [string]$response.Content
    if ($response.StatusCode -ne 200 -or [string]::IsNullOrWhiteSpace($content)) {
      throw "empty or non-200 response status=$($response.StatusCode)"
    }
    $phase = 'write-body'
    Set-Content -LiteralPath $bodyPath -Value $content -Encoding utf8
    $phase = 'hash-body'
    $sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $bodyPath).Hash.ToLowerInvariant()
    $bytes = (Get-Item -LiteralPath $bodyPath).Length
    $phase = 'append-recovery-row'
    $recoveryRows.Add([pscustomobject]@{
      doc_id = $doc.doc_id
      language = $doc.language
      branch = $doc.branch
      lexeme_ids = $doc.lexeme_ids
      recovered_path = $relBody
      source_url = $doc.page_url
      raw_url = $uri
      bytes = $bytes
      sha256 = $sha
      recovery_status = 'source-body-downloaded'
      source_use_status = 'external source-canon candidate; not row-verified; not counted in branch weights'
      claim_boundary = 'no native review; no accepted terminology; no source certification; no license-clearance claim'
    }) | Out-Null
    $phase = 'append-source-doc-row'
    $sourceDocRows.Add([pscustomobject]@{
      doc_id = $doc.doc_id
      path = $relBody
      language = $doc.language
      branch = $doc.branch
      file_type = 'wikitext'
      provenance_url_or_path = $doc.page_url
      sha256 = $sha
      license_or_availability_note = 'Wikimedia raw page source; see source_witnesses/external_wikimedia_recovery/20260705/wikimedia_access_license_signal.csv; no license-clearance claim'
      witness_category = 'source-witness; external-wikimedia-recovery; not row-verified relation/function attestation'
    }) | Out-Null
    $phase = 'append-coverage-rows'
    foreach ($lexeme in ($doc.lexeme_ids -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' })) {
      $coverageRows.Add([pscustomobject]@{
        lexeme_id = $lexeme
        doc_id = $doc.doc_id
        language = $doc.language
        branch = $doc.branch
        source_path = $relBody
        source_url = $doc.page_url
        candidate_use = 'source-canon candidate for owner/source check'
        counted_in_branch_weight = 'no'
        next_action = 'language owner or support lane should verify formula-neighboring context before forms.csv or branch_weight_ledger promotion'
      }) | Out-Null
    }
  } catch {
    $blockerRows.Add([pscustomobject]@{
      doc_id = $doc.doc_id
      language = $doc.language
      branch = $doc.branch
      lexeme_ids = $doc.lexeme_ids
      source_url = $doc.page_url
      raw_url = $uri
      blocker = "phase=$phase; $($_.Exception.Message)"
      next_action = 'retry slowly or locate alternate source archive/body'
      claim_boundary = 'not recovered; no witness claim'
    }) | Out-Null
  }
  Start-Sleep -Milliseconds 1500
}

Export-CsvRows 'external_wikimedia_source_recovery.csv' $recoveryRows
Export-CsvRows 'external_wikimedia_candidate_coverage.csv' $coverageRows
Export-CsvRows 'external_wikimedia_blockers.csv' $blockerRows

$sourceDocsPath = Join-Path $ResolvedRoot 'source_documents.csv'
$existingSourceDocs = @(Import-Csv -LiteralPath $sourceDocsPath) | Where-Object {
  $id = $_.doc_id
  -not (@($docs | ForEach-Object { $_.doc_id }) -contains $id)
}
($existingSourceDocs + $sourceDocRows) | Export-Csv -LiteralPath $sourceDocsPath -NoTypeInformation -Encoding utf8

$sourceAcqPath = Join-Path $ResolvedRoot 'source_acquisition_recovery.csv'
$existingAcqRows = @(Import-Csv -LiteralPath $sourceAcqPath) | Where-Object {
  $id = $_.recovery_id
  -not (@($docs | ForEach-Object { $_.doc_id }) -contains $id)
}
$newAcqRows = foreach ($row in $recoveryRows) {
  [pscustomobject]@{
    recovery_id = $row.doc_id
    language = $row.language
    branch = $row.branch
    recovered_path = $row.recovered_path
    source_status = $row.recovery_status
    relation_function_status = 'not row-verified; external source-canon candidate only'
    next_action = 'verify context before adding forms or branch-weight evidence'
    caveat = 'not approval, not accepted terminology, not translation completion'
  }
}
($existingAcqRows + $newAcqRows) | Export-Csv -LiteralPath $sourceAcqPath -NoTypeInformation -Encoding utf8

$summary = @"
# External Wikimedia Source Recovery 20260705

Status: source-canon candidate support only.

Recovered source bodies: $($recoveryRows.Count)
Blocked or missing bodies: $($blockerRows.Count)
Candidate coverage rows: $($coverageRows.Count)

These files were recovered through low-rate raw page exports for Polish and Ukrainian Wikimedia pages relevant to relation/function gap rows. They are packaged as source-canon candidates for language-owner/source checks. They are not counted in `branch_weight_ledger.csv`, not appended to `forms.csv`, and do not create native review, accepted terminology, source certification, license clearance, or translation completion.
"@
Set-Content -LiteralPath (Join-Path $ResolvedRoot 'generated-draft\external_wikimedia_source_recovery_handoff.md') -Value $summary -Encoding utf8

Add-Content -LiteralPath (Join-Path $ResolvedRoot 'SESSION_LOGBOOK_20260705.md') -Value "`nExternal Wikimedia recovery addendum: recovered $($recoveryRows.Count) Polish/Ukrainian raw wikitext source bodies and $($coverageRows.Count) candidate coverage rows under external_wikimedia_* ledgers. These are source-canon candidates only and are not counted in branch weights or forms until context verification."

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
        if ($rel -match 'ledger|languages|source_documents|forms|weights|intelligibility|do_not_use|recovery|probe|candidate|blocker|measure|summary|scaffold|route|handoff|queue|audit|contexts|PRETRANSLATION|acknowledgement|ACKNOWLEDGED|B3_PACKAGE') { 'audit-ledger' } else { 'methodology' }
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

"WIKIMEDIA_RECOVERED $($recoveryRows.Count)"
"WIKIMEDIA_BLOCKERS $($blockerRows.Count)"
"WIKIMEDIA_COVERAGE_ROWS $($coverageRows.Count)"
"MANIFEST_ROWS $((Import-Csv -LiteralPath $manifestPath | Measure-Object).Count)"
