param()

$ErrorActionPreference = 'Stop'
$outputRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$koRoot = Join-Path $outputRoot 'ko'
$sourcePath = '${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\language_management\cjk\03_working_translations\noether_paper42_zh_translation_001_20260722\source\Noether_Paper42_CurrentGermanAuthority_interval.tex'
$sourceExpectedHash = 'B6BB3A6267BA8495FC19914A72768351E4923B13374634701AF3CBDE659883CC'
$historicalWholeHash = '443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27'
$utf8 = [System.Text.UTF8Encoding]::new($false)
$sha = [System.Security.Cryptography.SHA256]::Create()

$rowsText = @'
structural_id|structure_type|source_start|source_end|unit_id|target_start|target_end|parent_id|order|crossrefs|label
NOE-P42-KO-WORK-001|work|1|230|U01|8|21||1||Paper 42 translated-work root
NOE-P42-KO-TITLE-001|title|1|1|U01|8|8|NOE-P42-KO-WORK-001|2||Paper title
NOE-P42-KO-PUB-001|publication_note|3|5|U01|10|12|NOE-P42-KO-WORK-001|3||Publication venue and pages
NOE-P42-KO-INTRO-PARA-001|paragraph|7|7|U01|14|14|NOE-P42-KO-WORK-001|4|NOE-P42-KO-SEC-I-001;NOE-P42-KO-SEC-II-001;NOE-P42-KO-SEC-III-001|Programmatic introduction
NOE-P42-KO-NOTE-001|note|7|7|U01|14|14|NOE-P42-KO-INTRO-PARA-001|5||Footnote 1 crossed-product and maximal-order references
NOE-P42-KO-BIB-001|bibliography_item|7|7|U01|14|14|NOE-P42-KO-NOTE-001|6||Hasse 1932 cyclic algebras
NOE-P42-KO-BIB-002|bibliography_item|7|7|U01|14|14|NOE-P42-KO-NOTE-001|7||Hasse 1931 p-adic division algebras
NOE-P42-KO-NOTE-002|note|7|7|U01|14|14|NOE-P42-KO-INTRO-PARA-001|8||Footnote 2 provenance of explicit representations
NOE-P42-KO-INTRO-PARA-002|paragraph|9|9|U01|16|16|NOE-P42-KO-WORK-001|9||Chevalley and Hasse scope note
NOE-P42-KO-NOTE-003|note|9|9|U01|16|16|NOE-P42-KO-INTRO-PARA-002|10||Footnote 3 Chevalley citation
NOE-P42-KO-BIB-003|bibliography_item|9|9|U01|16|16|NOE-P42-KO-NOTE-003|11||Chevalley 1934 simple-algebra ideals
NOE-P42-KO-NOTE-004|note|9|9|U01|16|16|NOE-P42-KO-INTRO-PARA-002|12||Footnote 4 Hasse preceding paper
NOE-P42-KO-BIB-004|bibliography_item|9|9|U01|16|16|NOE-P42-KO-NOTE-004|13||Hasse certain ideals in a simple algebra
NOE-P42-KO-SEC-I-001|section|11|14|U01|18|21|NOE-P42-KO-WORK-001|14||Section I matrix units and dual bases
NOE-P42-KO-SEC-I-SUB-001|subsection|16|16|U02|8|8|NOE-P42-KO-SEC-I-001|15||Section I.1 factor system one
NOE-P42-KO-EQ-001|equation|17|19|U02|9|11|NOE-P42-KO-SEC-I-SUB-001|16||Crossed-product decomposition and multiplication
NOE-P42-KO-EQ-002|equation|20|22|U02|12|14|NOE-P42-KO-SEC-I-SUB-001|17||Operator commutation relation
NOE-P42-KO-PARA-003|paragraph|23|27|U02|15|19|NOE-P42-KO-SEC-I-SUB-001|18|NOE-P42-KO-EQ-003|Definition of E_G
NOE-P42-KO-EQ-003|equation|24|26|U02|16|18|NOE-P42-KO-PARA-003|19||E_G sum definition
NOE-P42-KO-EQ-004|equation|28|28|U02|20|20|NOE-P42-KO-SEC-I-SUB-001|20||Equation 1 trivial-representation relation
NOE-P42-KO-NOTE-005|note|29|29|U02|21|21|NOE-P42-KO-EQ-004|21||Footnote 5 characteristic and idempotent
NOE-P42-KO-EQ-005|equation|30|30|U02|22|22|NOE-P42-KO-SEC-I-SUB-001|22||Equation 2a
NOE-P42-KO-EQ-006|equation|31|31|U02|23|23|NOE-P42-KO-SEC-I-SUB-001|23||Equation 2b trace relation
NOE-P42-KO-PARA-004|paragraph|32|32|U02|24|24|NOE-P42-KO-SEC-I-SUB-001|24|NOE-P42-KO-THM-I-001|Trace interpretation and theorem bridge
NOE-P42-KO-THM-I-001|theorem|34|39|U02|26|31|NOE-P42-KO-SEC-I-SUB-001|25|NOE-P42-KO-EQ-007|Matrix-unit theorem
NOE-P42-KO-EQ-007|equation|36|39|U02|28|31|NOE-P42-KO-THM-I-001|26||Module-product display
NOE-P42-KO-PROOF-I-001|proof|40|47|U02|32|39|NOE-P42-KO-THM-I-001|27|NOE-P42-KO-EQ-008|Proof of matrix-unit theorem
NOE-P42-KO-EQ-008|equation|41|46|U02|33|38|NOE-P42-KO-PROOF-I-001|28||Matrix-unit multiplication display
NOE-P42-KO-REM-I-001|remark|49|49|U02|41|41|NOE-P42-KO-SEC-I-SUB-001|29||Remark 1 scalar extension
NOE-P42-KO-REM-I-002|remark|51|51|U02|43|43|NOE-P42-KO-SEC-I-SUB-001|30||Remark 2 nonzero ideal argument
NOE-P42-KO-SEC-I-SUB-002|subsection|53|74|U03|8|29|NOE-P42-KO-SEC-I-001|31||Section I.2 non-Galois splitting field
NOE-P42-KO-EQ-009|equation|55|60|U03|10|15|NOE-P42-KO-SEC-I-SUB-002|32||Coset decomposition and E_H
NOE-P42-KO-EQ-010|equation|61|65|U03|16|20|NOE-P42-KO-SEC-I-SUB-002|33||E_G and u_Si definitions
NOE-P42-KO-PARA-005|paragraph|66|66|U03|21|21|NOE-P42-KO-SEC-I-SUB-002|34|NOE-P42-KO-EQ-011;NOE-P42-KO-EQ-012;NOE-P42-KO-EQ-013|Relations bridge
NOE-P42-KO-EQ-011|equation|67|67|U03|22|22|NOE-P42-KO-SEC-I-SUB-002|35||Equation 3
NOE-P42-KO-EQ-012|equation|68|68|U03|23|23|NOE-P42-KO-SEC-I-SUB-002|36||Equation 4
NOE-P42-KO-EQ-013|equation|69|69|U03|24|24|NOE-P42-KO-SEC-I-SUB-002|37||Equation 5
NOE-P42-KO-PROOF-I-002|proof|70|72|U03|25|27|NOE-P42-KO-SEC-I-SUB-002|38|NOE-P42-KO-EQ-014|Proof of relations 3 through 5 and 1 prime
NOE-P42-KO-EQ-014|equation|71|71|U03|26|26|NOE-P42-KO-PROOF-I-002|39||Equation 1 prime
NOE-P42-KO-PARA-006|paragraph|74|74|U03|29|29|NOE-P42-KO-SEC-I-SUB-002|40|NOE-P42-KO-THM-I-001|Conclusion K equals k E_G k
NOE-P42-KO-SEC-I-SUB-003|subsection|76|88|U04|8|20|NOE-P42-KO-SEC-I-001|41||Section I.3 corner algebra
NOE-P42-KO-PARA-007|paragraph|77|79|U04|9|11|NOE-P42-KO-SEC-I-SUB-003|42|NOE-P42-KO-NOTE-006|Non-split transition and rank argument
NOE-P42-KO-NOTE-006|note|77|77|U04|9|9|NOE-P42-KO-PARA-007|43||Footnote 6 prospective non-Galois analogue
NOE-P42-KO-EQ-015|equation|80|88|U04|12|20|NOE-P42-KO-SEC-I-SUB-003|44||Corner-algebra aligned calculation
NOE-P42-KO-SEC-II-001|section|90|93|U05|8|11|NOE-P42-KO-WORK-001|45||Section II maximal orders and regions
NOE-P42-KO-PARA-008|paragraph|95|95|U05|13|13|NOE-P42-KO-SEC-II-001|46|NOE-P42-KO-NOTE-007|Number-field setup and dual modules
NOE-P42-KO-NOTE-007|note|95|95|U05|13|13|NOE-P42-KO-PARA-008|47||Footnote 7 function-field extension
NOE-P42-KO-THM-II-001|theorem|97|98|U05|15|16|NOE-P42-KO-SEC-II-001|48|NOE-P42-KO-PROOF-II-001|Theorem II.1 maximal order
NOE-P42-KO-THM-II-002|theorem|100|101|U05|18|19|NOE-P42-KO-SEC-II-001|49|NOE-P42-KO-PROOF-II-002|Theorem II.2 reciprocal ideals
NOE-P42-KO-REM-II-001|remark|103|103|U05|21|21|NOE-P42-KO-THM-II-002|50||Remark trace pairing and reciprocity
NOE-P42-KO-THM-II-003|theorem|105|106|U05|23|24|NOE-P42-KO-SEC-II-001|51|NOE-P42-KO-PROOF-II-003|Theorem II.3 all ideals and maximal orders
NOE-P42-KO-THM-II-004|theorem|108|109|U05|26|27|NOE-P42-KO-SEC-II-001|52|NOE-P42-KO-PROOF-II-004|Theorem II.4 region classification
NOE-P42-KO-THM-II-004A|theorem|111|112|U05|29|30|NOE-P42-KO-SEC-II-001|53|NOE-P42-KO-PROOF-II-004A|Theorem II.4a principal region
NOE-P42-KO-PARA-009|paragraph|114|114|U06|8|8|NOE-P42-KO-SEC-II-001|54|NOE-P42-KO-LEM-II-001|Localization setup
NOE-P42-KO-LEM-II-001|lemma|116|117|U06|10|11|NOE-P42-KO-SEC-II-001|55|NOE-P42-KO-NOTE-008;NOE-P42-KO-COR-II-001|Intersection of localized modules
NOE-P42-KO-NOTE-008|note|117|117|U06|11|11|NOE-P42-KO-LEM-II-001|56||Footnote 8 p-adic version
NOE-P42-KO-COR-II-001|corollary|119|119|U06|13|13|NOE-P42-KO-LEM-II-001|57||Corollaries on components and maximality
NOE-P42-KO-PROOF-II-001|proof|121|137|U07|8|24|NOE-P42-KO-THM-II-001|58|NOE-P42-KO-EQ-016;NOE-P42-KO-EQ-017|Proof of Theorem II.1
NOE-P42-KO-EQ-016|equation|123|130|U07|10|17|NOE-P42-KO-PROOF-II-001|59|NOE-P42-KO-NOTE-009|Order closure and trace ideal
NOE-P42-KO-NOTE-009|note|130|130|U07|17|17|NOE-P42-KO-EQ-016|60||Footnote 9 trace ideal definition
NOE-P42-KO-EQ-017|equation|134|136|U07|21|23|NOE-P42-KO-PROOF-II-001|61||Localized matrix order
NOE-P42-KO-REM-II-002|remark|139|139|U07|26|26|NOE-P42-KO-THM-II-001|62||Remark trace ideal equals base ring
NOE-P42-KO-PROOF-II-002|proof|141|160|U08|8|27|NOE-P42-KO-THM-II-002|63|NOE-P42-KO-EQ-018|Proof of Theorem II.2
NOE-P42-KO-EQ-018|equation|143|160|U08|10|27|NOE-P42-KO-PROOF-II-002|64||Four reciprocal-ideal identities
NOE-P42-KO-PROOF-II-003|proof|162|179|U09|8|26|NOE-P42-KO-THM-II-003|65|NOE-P42-KO-EQ-019;NOE-P42-KO-NOTE-010;NOE-P42-KO-EQ-022|Proof of Theorem II.3
NOE-P42-KO-EQ-019|equation|164|167|U09|10|13|NOE-P42-KO-PROOF-II-003|66||Left-ideal generator display
NOE-P42-KO-NOTE-010|note|168|175|U09|14|22|NOE-P42-KO-PROOF-II-003|67|NOE-P42-KO-EQ-020;NOE-P42-KO-EQ-021|Footnote 10 non-Galois replacement
NOE-P42-KO-EQ-020|equation|169|171|U09|15|17|NOE-P42-KO-NOTE-010|68||Non-Galois E_G l display
NOE-P42-KO-EQ-021|equation|173|175|U09|19|21|NOE-P42-KO-NOTE-010|69||Non-Galois module decomposition
NOE-P42-KO-EQ-022|equation|176|178|U09|23|25|NOE-P42-KO-PROOF-II-003|70||E_G l_mu display
NOE-P42-KO-PROOF-II-004|proof|181|182|U10|8|9|NOE-P42-KO-THM-II-004|71||Proof of Theorem II.4
NOE-P42-KO-PROOF-II-004A|proof|184|185|U10|11|12|NOE-P42-KO-THM-II-004A|72||Proof of Theorem II.4a
NOE-P42-KO-SEC-III-001|section|187|189|U11|8|10|NOE-P42-KO-WORK-001|73||Section III arbitrary crossed products
NOE-P42-KO-PARA-010|paragraph|191|191|U11|12|12|NOE-P42-KO-SEC-III-001|74|NOE-P42-KO-DEF-III-001|General-case transition
NOE-P42-KO-DEF-III-001|definition|193|193|U11|14|14|NOE-P42-KO-SEC-III-001|75||Definition of a region and principal region
NOE-P42-KO-PARA-011|paragraph|195|195|U11|16|16|NOE-P42-KO-SEC-III-001|76|NOE-P42-KO-THM-III-001;NOE-P42-KO-THM-III-002|Theorem bridge
NOE-P42-KO-THM-III-001|theorem|197|198|U11|18|19|NOE-P42-KO-SEC-III-001|77||Theorem III.1 principal-region transformations
NOE-P42-KO-THM-III-002|theorem|200|201|U11|21|22|NOE-P42-KO-SEC-III-001|78|NOE-P42-KO-PROOF-III-001|Theorem III.2 prime degree
NOE-P42-KO-PROOF-III-001|proof|203|205|U11|24|26|NOE-P42-KO-THM-III-002|79|NOE-P42-KO-NOTE-011|Proof of Theorems III.1 and III.2
NOE-P42-KO-NOTE-011|note|203|203|U11|24|24|NOE-P42-KO-PROOF-III-001|80||Footnote 11 local-to-global reference
NOE-P42-KO-PARA-012|paragraph|207|207|U11|28|28|NOE-P42-KO-SEC-III-001|81|NOE-P42-KO-THM-III-003|Further theorem bridge
NOE-P42-KO-THM-III-003|theorem|209|210|U11|30|31|NOE-P42-KO-SEC-III-001|82||Theorem III.3 arbitrary region
NOE-P42-KO-PARA-013|paragraph|212|212|U11|33|33|NOE-P42-KO-THM-III-003|83||Local operator replacement
NOE-P42-KO-PARA-014|paragraph|214|214|U11|35|35|NOE-P42-KO-SEC-III-001|84|NOE-P42-KO-NOTE-012|Existence of a principal region
NOE-P42-KO-NOTE-012|note|214|214|U11|35|35|NOE-P42-KO-PARA-014|85||Footnote 12 Hasse and Chevalley alternative proof
NOE-P42-KO-BIB-005|bibliography_item|214|214|U11|35|35|NOE-P42-KO-NOTE-012|86||Hasse and Chevalley cross-references
NOE-P42-KO-PARA-015|paragraph|216|216|U12|8|8|NOE-P42-KO-WORK-001|87||Closing characterization questions
NOE-P42-KO-EX-001|example|218|226|U12|10|18|NOE-P42-KO-WORK-001|88|NOE-P42-KO-EQ-023;NOE-P42-KO-EQ-024|Quaternion maximal-order example
NOE-P42-KO-EQ-023|equation|219|221|U12|11|13|NOE-P42-KO-EX-001|89||Quaternion maximal order
NOE-P42-KO-EQ-024|equation|223|225|U12|15|17|NOE-P42-KO-EX-001|90||Third-root field order
NOE-P42-KO-PLACE-DATE-001|place_date|228|230|U12|20|22|NOE-P42-KO-WORK-001|91||Göttingen August 1932
'@

$rows = $rowsText | ConvertFrom-Csv -Delimiter '|'
$sourceLines = [System.IO.File]::ReadAllLines($sourcePath, $utf8)
$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()
$sourceActualHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash
if ($sourceActualHash -ne $sourceExpectedHash) { $errors.Add("source hash mismatch: $sourceActualHash") }

$ids = @{}
foreach ($row in $rows) {
  if ($ids.ContainsKey($row.structural_id)) { $errors.Add("duplicate structural_id $($row.structural_id)") }
  $ids[$row.structural_id] = $true
}

$records = [System.Collections.Generic.List[object]]::new()
foreach ($row in $rows) {
  $sourceStart = [int]$row.source_start
  $sourceEnd = [int]$row.source_end
  $targetStart = [int]$row.target_start
  $targetEnd = [int]$row.target_end
  if ($sourceStart -gt $sourceEnd -or $sourceEnd -gt $sourceLines.Count) { $errors.Add("bad source locator $($row.structural_id)") }
  if ($row.parent_id -and -not $ids.ContainsKey($row.parent_id)) { $errors.Add("missing parent $($row.parent_id) for $($row.structural_id)") }
  $crossrefs = @()
  if ($row.crossrefs) {
    $crossrefs = @($row.crossrefs -split ';')
    foreach ($crossref in $crossrefs) { if (-not $ids.ContainsKey($crossref)) { $errors.Add("missing crossref $crossref for $($row.structural_id)") } }
  }
  $unitNumber = [int]$row.unit_id.Substring(1)
  $targetName = 'Noether_Paper42_Korean_U{0:D2}_translation_draft_v001.tex' -f $unitNumber
  $targetPath = Join-Path $koRoot $targetName
  if (-not (Test-Path -LiteralPath $targetPath)) { $errors.Add("missing target $targetPath"); continue }
  $targetLines = [System.IO.File]::ReadAllLines($targetPath, $utf8)
  if ($targetStart -gt $targetEnd -or $targetEnd -gt $targetLines.Count) { $errors.Add("bad target locator $($row.structural_id)") }
  $sourceText = (($sourceLines[($sourceStart - 1)..($sourceEnd - 1)] -join "`n") + "`n")
  $sourceBytes = $utf8.GetBytes($sourceText)
  $sourceHash = [Convert]::ToHexString($sha.ComputeHash($sourceBytes))
  $targetText = (($targetLines[($targetStart - 1)..($targetEnd - 1)] -join "`n") + "`n")
  $targetBytes = $utf8.GetBytes($targetText)
  $targetHash = [Convert]::ToHexString($sha.ComputeHash($targetBytes))
  $targetFile = Get-Item -LiteralPath $targetPath
  $targetFileHash = (Get-FileHash -LiteralPath $targetPath -Algorithm SHA256).Hash
  $record = [ordered]@{
    structural_id = $row.structural_id
    structure_type = $row.structure_type
    label = $row.label
    parent_id = $(if ($row.parent_id) { $row.parent_id } else { $null })
    order = [int]$row.order
    cross_reference_ids = $crossrefs
    authority = [ordered]@{
      snapshot_path = $sourcePath
      snapshot_bytes = 23912
      snapshot_sha256 = $sourceExpectedHash
      historical_whole_sha256 = $historicalWholeHash
      pointer_state = 'replacement_pending_from_canon_owner'
    }
    source_locator = [ordered]@{
      local_line_start = $sourceStart
      local_line_end = $sourceEnd
      lf_bytes = $sourceBytes.Length
      lf_sha256 = $sourceHash
    }
    target_locator = [ordered]@{
      unit_id = $row.unit_id
      path = $targetPath
      line_start = $targetStart
      line_end = $targetEnd
      file_bytes = [int64]$targetFile.Length
      file_sha256 = $targetFileHash
      lf_bytes = $targetBytes.Length
      lf_sha256 = $targetHash
    }
    language = 'ko-KR'
    completion_state = 'translated_producer_draft'
    review_state = 'independent_check_absent'
    publication_state = 'private_working'
    alignment_state = 'producer_structural_pair_unchecked'
    continuation_cursor = "after stored-source line $sourceEnd"
  }
  $records.Add([pscustomobject]$record)
}

$jsonlPath = Join-Path $PSScriptRoot 'PRODUCER_STRUCTURAL_INDEX.jsonl'
$csvPath = Join-Path $PSScriptRoot 'PRODUCER_STRUCTURAL_INDEX.csv'
$reportPath = Join-Path $PSScriptRoot 'PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json'
$jsonLines = foreach ($record in $records) { $record | ConvertTo-Json -Depth 8 -Compress }
[System.IO.File]::WriteAllLines($jsonlPath, $jsonLines, $utf8)
$projection = foreach ($record in $records) {
  [pscustomobject]@{
    structural_id = $record.structural_id
    structure_type = $record.structure_type
    label = $record.label
    parent_id = $record.parent_id
    order = $record.order
    cross_reference_ids = ($record.cross_reference_ids -join ';')
    source_line_start = $record.source_locator.local_line_start
    source_line_end = $record.source_locator.local_line_end
    source_lf_sha256 = $record.source_locator.lf_sha256
    target_unit = $record.target_locator.unit_id
    target_path = $record.target_locator.path
    target_line_start = $record.target_locator.line_start
    target_line_end = $record.target_locator.line_end
    target_file_sha256 = $record.target_locator.file_sha256
    target_lf_sha256 = $record.target_locator.lf_sha256
    language = $record.language
    completion_state = $record.completion_state
    review_state = $record.review_state
    publication_state = $record.publication_state
    continuation_cursor = $record.continuation_cursor
  }
}
$csvText = $projection | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($csvPath, $csvText, $utf8)

$requiredTypes = @('work','title','publication_note','section','subsection','paragraph','theorem','lemma','corollary','definition','remark','proof','equation','note','bibliography_item','example','place_date')
foreach ($requiredType in $requiredTypes) {
  if (-not ($records.structure_type -contains $requiredType)) { $errors.Add("missing required structure type $requiredType") }
}
$report = [ordered]@{
  status = $(if ($errors.Count -eq 0) { 'pass' } else { 'fail' })
  record_count = $records.Count
  unique_id_count = ($records.structural_id | Sort-Object -Unique).Count
  source_snapshot_sha256 = $sourceActualHash
  latest_structural_id = $(if ($records.Count) { $records[-1].structural_id } else { $null })
  errors = @($errors)
  warnings = @($warnings)
  validation_scope = 'producer metadata integrity only; no source, translation, formula, build, render, or publication validation'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 6), $utf8)
if ($errors.Count -gt 0) { throw "structural index validation failed with $($errors.Count) errors" }
$report | ConvertTo-Json -Depth 6
