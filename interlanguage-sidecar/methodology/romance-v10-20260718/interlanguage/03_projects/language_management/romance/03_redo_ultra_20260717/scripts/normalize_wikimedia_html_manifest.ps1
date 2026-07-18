$ErrorActionPreference='Stop'
$here=Split-Path -Parent $MyInvocation.MyCommand.Path
$root=Split-Path -Parent $here
$corpus=Join-Path $root 'corpus'
$manifestPath=Join-Path $corpus 'WIKIMEDIA_HTML_CORPUS_MANIFEST_v1.csv'
$coveragePath=Join-Path $corpus 'WIKIMEDIA_HTML_COVERAGE_v1.csv'
$queryPath=Join-Path $corpus 'WIKIMEDIA_HTML_QUERY_LOG_v1.csv'
$rejectedPath=Join-Path $corpus 'WIKIMEDIA_HTML_REJECTED_AUTOMATIC_SEARCH_v1.csv'
$prov=Join-Path $corpus '_provenance';New-Item -ItemType Directory -Force -Path $prov|Out-Null
if(!(Test-Path (Join-Path $prov 'WIKIMEDIA_HTML_CORPUS_MANIFEST_v1_PRE_QA.csv'))){Copy-Item -LiteralPath $manifestPath -Destination (Join-Path $prov 'WIKIMEDIA_HTML_CORPUS_MANIFEST_v1_PRE_QA.csv')}
if(!(Test-Path (Join-Path $prov 'WIKIMEDIA_HTML_COVERAGE_v1_PRE_QA.csv'))){Copy-Item -LiteralPath $coveragePath -Destination (Join-Path $prov 'WIKIMEDIA_HTML_COVERAGE_v1_PRE_QA.csv')}

$raw=Import-Csv $manifestPath
$invalid=@($raw|Where-Object { [int64]$_.page_id -eq 0 -or [int64]$_.revision_id -eq 0 })
$candidate=foreach($r in $raw|Where-Object { [int64]$_.page_id -gt 0 -and [int64]$_.revision_id -gt 0 }){
  $title=$r.title;$provenance='existing_manifest'
  if([string]::IsNullOrWhiteSpace($title)){
    $path=Join-Path $root ($r.local_relative_path -replace '/','\')
    $html=[System.IO.File]::ReadAllText($path)
    $m=[regex]::Match($html,'"wgTitle":"([^"]+)"')
    if($m.Success){$title=[System.Text.RegularExpressions.Regex]::Unescape($m.Groups[1].Value);$provenance='saved_page_wgTitle_metadata'}
  }
  if([string]::IsNullOrWhiteSpace($title)){$title=$r.query;$provenance='query_fallback_REVIEW_REQUIRED'}
  [pscustomobject][ordered]@{
    source_id=$r.source_id;language_code=$r.language_code;query=$r.query;title=$title;title_provenance=$provenance
    page_id=$r.page_id;revision_id=$r.revision_id;source_url=$r.source_url;retrieved_url=$r.retrieved_url;license_url=$r.license_url
    local_relative_path=$r.local_relative_path;bytes=$r.bytes;sha256=$r.sha256;source_use_status=$r.source_use_status;sense_review_status=$r.sense_review_status
  }
}
$newRomanshNonMathematical=@($candidate|Where-Object {
  $_.language_code -eq 'rm' -and $_.page_id -in @('12989','10695','13415')
})
$priorRomanshNonMathematical=@()
if(Test-Path $rejectedPath){$priorRomanshNonMathematical=@(Import-Csv $rejectedPath)}
$romanshNonMathematical=if($newRomanshNonMathematical.Count){$newRomanshNonMathematical}else{$priorRomanshNonMathematical}
$valid=@($candidate|Where-Object {
  !($_.language_code -eq 'rm' -and $_.page_id -in @('12989','10695','13415'))
})

$romanshNonMathematical|ForEach-Object {
  [pscustomobject][ordered]@{
    source_id=$_.source_id;language_code=$_.language_code;query=$_.query;title=$_.title
    page_id=$_.page_id;revision_id=$_.revision_id;source_url=$_.source_url;retrieved_url=$_.retrieved_url
    local_relative_path=$_.local_relative_path;bytes=$_.bytes;sha256=$_.sha256
    rejection_reason='nonmathematical_automatic_search_result';review_status='manually_quarantined_20260717'
  }
}|Sort-Object query|Export-Csv -NoTypeInformation -Encoding utf8 $rejectedPath
$valid|Sort-Object language_code,query|Export-Csv -NoTypeInformation -Encoding utf8 $manifestPath

$q=Import-Csv $queryPath
foreach($bad in $invalid){
  foreach($qr in $q|Where-Object { $_.language -eq $bad.language_code -and $_.query -eq $bad.query }){$qr.status='no_article_result_zero_page_or_revision';$qr.url=''}
}
foreach($bad in $romanshNonMathematical){
  foreach($qr in $q|Where-Object { $_.language -eq $bad.language_code -and $_.query -eq $bad.query }){
    $qr.status=('rejected_nonmathematical_result:'+($bad.title -replace '\s+','_'))
  }
}
$q|Export-Csv -NoTypeInformation -Encoding utf8 $queryPath
$queryZeroFailures=@($q|Where-Object status -eq 'no_article_result_zero_page_or_revision')
$historicalPreQaPath=Join-Path $prov 'WIKIMEDIA_HTML_CORPUS_MANIFEST_v1_PRE_QA.csv'
$historicalPreQaRows=if(Test-Path $historicalPreQaPath){@(Import-Csv $historicalPreQaPath)}else{@($raw)}

$coverage=foreach($lang in ($q.language|Sort-Object -Unique)){
  $requested=@($q|Where-Object language -eq $lang).Count
  $rows=@($valid|Where-Object language_code -eq $lang)
  $byteSum=($rows.bytes|Measure-Object -Sum).Sum
  if($null -eq $byteSum){$byteSum=0}
  $status=if($lang -eq 'rm' -and $rows.Count -eq 0){'explicit_zero_mathematics_body_gap'}else{'active_topic_checked_rows'}
  [pscustomobject]@{language_code=$lang;requested=$requested;downloaded=$rows.Count;unique_pages=@($rows.page_id|Sort-Object -Unique).Count;bytes=$byteSum;coverage_status=$status;license_urls=($rows.license_url|Sort-Object -Unique)-join ';'}
}
$coverage|Export-Csv -NoTypeInformation -Encoding utf8 $coveragePath

$report=[ordered]@{
  artifact='WIKIMEDIA_HTML_MANIFEST_QA';input_rows=$raw.Count;historical_pre_qa_rows=$historicalPreQaRows.Count;active_rows=$valid.Count
  excluded_zero_rows=$invalid.Count;quarantined_nonmathematical_rows=$romanshNonMathematical.Count
  blank_titles_after=(@($valid|Where-Object {[string]::IsNullOrWhiteSpace($_.title)}).Count)
  romansh_downloaded=0;romansh_unique_pages=0;romansh_status='explicit_zero_mathematics_body_gap'
  query_log_zero_failure_count=$queryZeroFailures.Count
  query_log_zero_failure_queries=@($queryZeroFailures|ForEach-Object query)
  quarantined_queries=@($romanshNonMathematical|ForEach-Object query)
}
$report|ConvertTo-Json|Set-Content -Encoding utf8 (Join-Path $corpus 'WIKIMEDIA_HTML_MANIFEST_QA_v1.json')
$report|ConvertTo-Json
