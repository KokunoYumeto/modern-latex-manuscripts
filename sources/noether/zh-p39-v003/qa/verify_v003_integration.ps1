$ErrorActionPreference = 'Stop'

$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$recordPath = Join-Path $root 'qa\PRODUCER_V003_VALIDATION_RECORD.json'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$failures = [System.Collections.Generic.List[object]]::new()
$checks = [System.Collections.Generic.List[object]]::new()

function Add-Check([string]$name, [bool]$pass, $observed, $expected) {
    $checks.Add([ordered]@{ name = $name; pass = $pass; observed = $observed; expected = $expected })
    if (-not $pass) { $failures.Add([ordered]@{ check = $name; observed = $observed; expected = $expected }) }
}

function Pin([string]$relative, [int64]$bytes, [string]$sha256) {
    $path = Join-Path $root $relative
    $exists = Test-Path -LiteralPath $path -PathType Leaf
    $actualBytes = if ($exists) { (Get-Item -LiteralPath $path).Length } else { -1 }
    $actualHash = if ($exists) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash } else { $null }
    Add-Check "pin:$relative" ($exists -and $actualBytes -eq $bytes -and $actualHash -eq $sha256) ([ordered]@{ bytes = $actualBytes; sha256 = $actualHash }) ([ordered]@{ bytes = $bytes; sha256 = $sha256 })
}

function Byte-Equal([string]$left, [string]$right, [string]$name) {
    $a = [System.IO.File]::ReadAllBytes((Join-Path $root $left))
    $b = [System.IO.File]::ReadAllBytes((Join-Path $root $right))
    Add-Check $name ([System.Linq.Enumerable]::SequenceEqual($a, $b)) ([ordered]@{ left_bytes = $a.Length; right_bytes = $b.Length }) 'byte-for-byte equality'
}

Pin 'zh-Hans-CN\Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v003.tex' 16141 '101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6'
Pin 'zh-Hans-CN\Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v003.pdf' 261533 '367061323E97D9D7431B883D48F190A214A224D62F3901C8E01DD1BCA7125BA1'
Pin 'zh-Hant-controlled\Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex' 16322 'F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8'
Pin 'zh-Hant-controlled\Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v003.pdf' 274922 'A64F7461A4F4CE451CA7E153FF3C8D55854AD6BC730A7336FD6669F8170F38C8'
Pin 'evidence\PRODUCER_TERMINOLOGY_LEDGER.csv' 21658 '4772D0E74F590A5AF576900CC944259C95314C0F0A5D9A935D4259B4B4F4B591'
Pin 'evidence\ADVERSE_SENSE_LEDGER.csv' 14068 '66D5441C0D1543BE28136EF679D887C54B74369F858F79CDC4C6C2A000E2F0CB'
Pin 'evidence\CJKV_CROSSWALK_P39_ZH.csv' 12893 'FBE968E86983F2435EEA335973254F8413C2E43B59544A797F0EC354DE260402'
Pin 'evidence\PRODUCER_CONCEPT_GRAPH.json' 49685 '348C0CD592F89E88E759AB6B3CEA79CC9DC2F5951764E8CDD1F3087FAB1BD83F'
Pin 'checker_return_v002\P39_V002_CHECKER_RETURN_RECEIPT.json' 7402 'B4E07772158637DE71A83E7F3A7AAF461840ACB89A19E0DE355EA5DC2390F046'
Pin 'checker_return_v002\P39_V002_RETURN_MANIFEST.sha256' 11584 '7FF46673A3DE1EDB3C3D7711C55CD5495313C1B8E501D5438C7D84BE32090F77'

Byte-Equal 'zh-Hans-CN\Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex' 'zh-Hans-CN\Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v003.tex' 'Hans_TeX_carried_byte_exact'
Byte-Equal 'zh-Hans-CN\Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf' 'zh-Hans-CN\Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v003.pdf' 'Hans_PDF_carried_byte_exact'
Byte-Equal 'checker_return_v002\candidates\zh-Hant-controlled\Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v002_checker_candidate.tex' 'zh-Hant-controlled\Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex' 'Hant_exact_checker_candidate'
Byte-Equal 'checker_return_v002\candidates\evidence\PRODUCER_TERMINOLOGY_LEDGER_checker_candidate.csv' 'evidence\PRODUCER_TERMINOLOGY_LEDGER.csv' 'terminology_exact_checker_candidate'
Byte-Equal 'checker_return_v002\candidates\evidence\ADVERSE_SENSE_LEDGER_checker_candidate.csv' 'evidence\ADVERSE_SENSE_LEDGER.csv' 'adverse_exact_checker_candidate'
Byte-Equal 'checker_return_v002\candidates\evidence\CJKV_CROSSWALK_P39_ZH_checker_candidate.csv' 'evidence\CJKV_CROSSWALK_P39_ZH.csv' 'crosswalk_exact_checker_candidate'
Byte-Equal 'checker_return_v002\candidates\evidence\PRODUCER_CONCEPT_GRAPH_checker_candidate.json' 'evidence\PRODUCER_CONCEPT_GRAPH.json' 'concept_graph_exact_checker_candidate'

$hant = [System.IO.File]::ReadAllText((Join-Path $root 'zh-Hant-controlled\Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex'), [System.Text.Encoding]::UTF8)
$badHypercomplex = ([string][char]0x8D85) + ([string][char]0x5FA9)
$badClassifier = ([string][char]0x4E00) + ([string][char]0x7B87)
$badStart = ([string][char]0x7740) + ([string][char]0x624B)
$badCounts = [ordered]@{
    rejected_hypercomplex = ([regex]::Matches($hant, [regex]::Escape($badHypercomplex))).Count
    rejected_classifier = ([regex]::Matches($hant, [regex]::Escape($badClassifier))).Count
    rejected_start_verb = ([regex]::Matches($hant, [regex]::Escape($badStart))).Count
}
Add-Check 'F001_rejected_forms_absent' (-not ($hant.Contains($badHypercomplex) -or $hant.Contains($badClassifier) -or $hant.Contains($badStart))) $badCounts 0
Add-Check 'controlled_generic_claim_marker' ($hant.Contains('Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose.')) $hant.Contains('Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose.') $true

$termRows = @(Import-Csv -LiteralPath (Join-Path $root 'evidence\PRODUCER_TERMINOLOGY_LEDGER.csv'))
$adverseRows = @(Import-Csv -LiteralPath (Join-Path $root 'evidence\ADVERSE_SENSE_LEDGER.csv'))
$crosswalkRows = @(Import-Csv -LiteralPath (Join-Path $root 'evidence\CJKV_CROSSWALK_P39_ZH.csv'))
Add-Check 'evidence_CSV_row_counts' ($termRows.Count -eq 20 -and $adverseRows.Count -eq 20 -and $crosswalkRows.Count -eq 20) ([ordered]@{ terminology = $termRows.Count; adverse = $adverseRows.Count; crosswalk = $crosswalkRows.Count }) ([ordered]@{ terminology = 20; adverse = 20; crosswalk = 20 })

$graph = Get-Content -LiteralPath (Join-Path $root 'evidence\PRODUCER_CONCEPT_GRAPH.json') -Raw | ConvertFrom-Json
$nodeIds = @{}; foreach ($node in $graph.nodes) { $nodeIds[$node.id] = $true }
$badEndpoints = @($graph.edges | Where-Object { -not $nodeIds.ContainsKey($_.from) -or -not $nodeIds.ContainsKey($_.to) })
Add-Check 'concept_graph_topology' ($graph.nodes.Count -eq 100 -and $graph.edges.Count -eq 100 -and $badEndpoints.Count -eq 0) ([ordered]@{ nodes = $graph.nodes.Count; edges = $graph.edges.Count; bad_endpoints = $badEndpoints.Count }) ([ordered]@{ nodes = 100; edges = 100; bad_endpoints = 0 })

$generation = Get-Content -LiteralPath (Join-Path $root 'qa\OPENCC_PRODUCER_RECORD_v003.json') -Raw | ConvertFrom-Json
Add-Check 'generation_record_exact_candidate_pin' ($generation.output_sha256 -eq 'F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8') $generation.output_sha256 'F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8'

$logText = Get-Content -LiteralPath (Join-Path $root 'zh-Hant-controlled\Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v003.log') -Raw
$logFlags = [ordered]@{
    fatal = ([regex]::Matches($logText, 'Fatal error')).Count
    emergency = ([regex]::Matches($logText, 'Emergency stop')).Count
    undefined_control = ([regex]::Matches($logText, 'Undefined control sequence')).Count
    overfull = ([regex]::Matches($logText, 'Overfull \\hbox')).Count
    underfull = ([regex]::Matches($logText, 'Underfull \\hbox')).Count
    missing_character = ([regex]::Matches($logText, 'Missing character')).Count
}
$flagTotal = 0; foreach ($value in $logFlags.Values) { $flagTotal += $value }
Add-Check 'Hant_final_log_flags' ($flagTotal -eq 0) $logFlags 0
Add-Check 'Hant_compiler_page_count' ($logText.Contains('(4 pages).')) $logText.Contains('(4 pages).') $true

$record = [ordered]@{
    schema_version = '1.0.0'
    record_type = 'NOETHER_P39_ZH_v003_producer_integration_validation'
    checker_return_id = 'ZHCHK-NOETHER-P39-V002-RETURN-001'
    checks_total = $checks.Count
    checks_passed = @($checks | Where-Object { $_.pass }).Count
    failure_count = $failures.Count
    all_pass = ($failures.Count -eq 0)
    checks = $checks
    failures = $failures
    claim_limit = 'Producer file-custody, exact-integration, data-shape, compiler-log, and page-count computation only; no PDF render/open/visual or independent linguistic/source validation.'
}
$json = ($record | ConvertTo-Json -Depth 12) + "`n"
[System.IO.File]::WriteAllText($recordPath, $json, $utf8NoBom)
$json
