param(
    [string]$Root = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$outPath = Join-Path $PSScriptRoot 'STRUCT.jsonl'
$authority = [ordered]@{
    authority_id = 'NOETH-DE-ED-0002'
    raw_sha256 = 'C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3'
    pointer_id = 'NOETH-DE-AUTH-v009-20260804'
    pointer_sha256 = 'B06BE3530D9CF2E82B56FDBA7FE41D5D044DF2425DFA2A059D4939EAA2F7A6C2'
}

function Get-RelativePath([string]$Path) {
    if ($Path.StartsWith($Root, [StringComparison]::OrdinalIgnoreCase)) {
        return $Path.Substring($Root.Length + 1).Replace('\', '/')
    }
    return $Path.Replace('\', '/')
}

function Add-Record([System.Collections.Generic.List[string]]$Rows, $Record) {
    $Rows.Add(($Record | ConvertTo-Json -Compress -Depth 30))
}

$unitSpecs = @(
    @{ file = 'JAPANESE_P31_U27_U30_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P31-U27-U30-20260804-001'; paper = 'P31'; kind = 'direct'; uncertainty = 'No source-span variant among authenticated compared heads; whole-head precedence remains separate.' },
    @{ file = 'JAPANESE_P31_U31_U32_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P31-U31-U32-20260804-001'; paper = 'P31'; kind = 'direct'; uncertainty = 'No source-span variant among authenticated compared heads; whole-head precedence remains separate.' },
    @{ file = 'JAPANESE_P31_U33_U34_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P31-U33-U34-20260804-001'; paper = 'P31'; kind = 'direct'; uncertainty = 'No source-span variant among authenticated compared heads; whole-head precedence remains separate.' },
    @{ file = 'KOREAN_P05_U01_U04_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P05-KO-U01-U04-20260804-001'; paper = 'P05'; kind = 'retained'; uncertainty = 'Exact current authority; predecessor emphasis-markup variants remain unadjudicated.' },
    @{ file = 'KOREAN_P07_U01_U08_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P07-KO-U01-U08-20260804-001'; paper = 'P07'; kind = 'retained'; uncertainty = 'Normalized-invariant selected/public predecessors; P09 remains structurally and editorially divergent.' },
    @{ file = 'KOREAN_P03_U01_U03_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P03-KO-U01-U03-20260804-001'; paper = 'P03'; kind = 'retained'; uncertainty = 'Raw or normalized invariant across all controlled heads.' },
    @{ file = 'KOREAN_P04_T01_T03_U01_U16_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T01-T03-U01-U16-20260804-001'; paper = 'P04'; kind = 'retained'; uncertainty = 'Exact current authority; predecessor notation and footnote variants remain explicit and unadjudicated.' },
    @{ file = 'KOREAN_P04_T04_T06_U17_U32_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T04-T06-U17-U32-20260804-001'; paper = 'P04'; kind = 'retained'; uncertainty = 'Exact current authority; predecessor notation, formula, and spacing variants remain explicit and unadjudicated.' },
    @{ file = 'KOREAN_P04_T07_U33_U38_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T07-U33-U38-20260804-001'; paper = 'P04'; kind = 'retained'; uncertainty = 'Exact current authority; predecessor expression and layout variants remain explicit and unadjudicated.' },
    @{ file = 'KOREAN_P04_T08_T09_U39_U50_AND_COMPLETE_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T08-T09-U39-U50-AND-COMPLETE-20260804-001'; paper = 'P04'; kind = 'retained'; uncertainty = 'Exact current authority with four complete-paper lineage classes preserved and no defect inference.' }
)

$rows = [System.Collections.Generic.List[string]]::new()
$sequence = 0
$lastByPaper = @{}

foreach ($spec in $unitSpecs) {
    $receiptPath = Join-Path (Join-Path $Root 'receipts') $spec.file
    $receiptSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $receiptPath).Hash
    $receipt = Get-Content -Raw -LiteralPath $receiptPath | ConvertFrom-Json

    if ($spec.kind -eq 'direct') {
        $units = @($receipt.units)
        $basePointer = '/units'
        $unitRoot = $null
    } else {
        $units = @($receipt.retained_normalized_units.units)
        $basePointer = '/retained_normalized_units/units'
        $unitRoot = $receipt.retained_normalized_units.root
    }

    for ($index = 0; $index -lt $units.Count; $index++) {
        $unit = $units[$index]
        $sequence++
        $recordId = 'NOETH-STR-{0:D3}' -f $sequence
        $coordinates = [ordered]@{}
        foreach ($property in $unit.PSObject.Properties) {
            if ($property.Name -notmatch '^(target_|opening$|snapshot_path$|file$)') {
                $coordinates[$property.Name] = $property.Value
            }
        }

        if ($unit.PSObject.Properties.Name -contains 'snapshot_path') {
            $artifactPath = $unit.snapshot_path
        } elseif ($unit.PSObject.Properties.Name -contains 'file') {
            $artifactPath = Join-Path $unitRoot $unit.file
        } else {
            throw "Unit $($unit.unit) in $($spec.file) has no retained artifact."
        }
        if (-not (Test-Path -LiteralPath $artifactPath)) {
            throw "Missing retained unit artifact: $artifactPath"
        }

        $artifactItem = Get-Item -LiteralPath $artifactPath
        $dependencies = @()
        if ($lastByPaper.ContainsKey($spec.paper)) {
            $dependencies = @($lastByPaper[$spec.paper])
        }
        $eol = if ($unit.PSObject.Properties.Name -contains 'bytes_lf_no_terminal') {
            'UTF-8 LF-normalized, no terminal newline'
        } else {
            'UTF-8 LF-normalized, terminal LF retained'
        }

        $record = [ordered]@{
            schema = 'noeth.struct.v1'
            record_id = $recordId
            object_type = 'source_unit'
            parent_unit_id = 'NOETH-' + $spec.paper
            parent_binder_id = $spec.binder
            order = $sequence
            label = [string]$unit.unit
            authority = $authority
            source_ref = [ordered]@{
                path = 'receipts/' + $spec.file
                locator = $basePointer + '/' + $index
                sha256 = $receiptSha
            }
            source_coordinates = $coordinates
            retained_artifact = [ordered]@{
                path = Get-RelativePath $artifactPath
                bytes = $artifactItem.Length
                sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $artifactPath).Hash
                eol_profile = $eol
            }
            dependencies = $dependencies
            cross_references = @()
            cross_reference_state = 'Not analyzed or inferred by coordinate-only canon control.'
            review_state = 'Exact source coordinates, bytes, and retained artifact hash replayed; target review remains outside this task.'
            uncertainty = $spec.uncertainty
            target_locator_state = 'lane_owned_not_collected_by_german_source_owner'
            indexing_limit = 'This record covers the declared closed source unit only; internal theorem, equation, note, and target structures were not silently inferred.'
        }
        Add-Record $rows $record
        $lastByPaper[$spec.paper] = $recordId
    }
}

$trancheSpecs = @(
    @{ file = 'KOREAN_P04_T01_T03_U01_U16_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T01-T03-U01-U16-20260804-001'; mode = 'array'; uncertainty = 'T01 invariant; T02-T03 have explicit unadjudicated predecessor variants.' },
    @{ file = 'KOREAN_P04_T04_T06_U17_U32_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T04-T06-U17-U32-20260804-001'; mode = 'array'; uncertainty = 'Exact current authority; predecessor variants remain explicit and unadjudicated.' },
    @{ file = 'KOREAN_P04_T07_U33_U38_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T07-U33-U38-20260804-001'; mode = 'single'; uncertainty = 'Exact current authority; predecessor variants remain explicit and unadjudicated.' },
    @{ file = 'KOREAN_P04_T08_T09_U39_U50_AND_COMPLETE_BINDER_20260804.json'; binder = 'NOETH-DE-BINDER-P04-KO-T08-T09-U39-U50-AND-COMPLETE-20260804-001'; mode = 'array_final'; uncertainty = 'Exact current authority; complete-paper lineage classes remain explicit and unadjudicated.' }
)

$lastTranche = $null
foreach ($spec in $trancheSpecs) {
    $receiptPath = Join-Path (Join-Path $Root 'receipts') $spec.file
    $receiptSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $receiptPath).Hash
    $receipt = Get-Content -Raw -LiteralPath $receiptPath | ConvertFrom-Json
    $items = @()

    if ($spec.mode -eq 'single') {
        $items = @([pscustomobject]@{
            label = 'T07'
            coordinates = $receipt.current_complete_interval
            pointer = '/current_complete_interval'
            artifact = $receipt.retained_normalized_units.complete
        })
    } else {
        for ($index = 0; $index -lt $receipt.current_tranches.Count; $index++) {
            $tranche = $receipt.current_tranches[$index]
            if ($spec.mode -eq 'array_final') {
                $artifact = @($receipt.retained_normalized_units.complete_files |
                    Where-Object { $_.role -eq $tranche.tranche })[0]
            } else {
                $artifact = @($receipt.retained_normalized_units.tranche_files |
                    Where-Object { $_.tranche -eq $tranche.tranche })[0]
            }
            $items += [pscustomobject]@{
                label = $tranche.tranche
                coordinates = $tranche
                pointer = '/current_tranches/' + $index
                artifact = $artifact
            }
        }
    }

    foreach ($item in $items) {
        $sequence++
        $recordId = 'NOETH-STR-{0:D3}' -f $sequence
        $artifactPath = Join-Path $receipt.retained_normalized_units.root $item.artifact.file
        if (-not (Test-Path -LiteralPath $artifactPath)) {
            throw "Missing retained tranche artifact: $artifactPath"
        }
        $artifactItem = Get-Item -LiteralPath $artifactPath
        $dependencies = @()
        if ($lastTranche) {
            $dependencies = @($lastTranche)
        }

        $record = [ordered]@{
            schema = 'noeth.struct.v1'
            record_id = $recordId
            object_type = 'tranche'
            parent_unit_id = 'NOETH-P04'
            parent_binder_id = $spec.binder
            order = $sequence
            label = [string]$item.label
            authority = $authority
            source_ref = [ordered]@{
                path = 'receipts/' + $spec.file
                locator = $item.pointer
                sha256 = $receiptSha
            }
            source_coordinates = $item.coordinates
            retained_artifact = [ordered]@{
                path = Get-RelativePath $artifactPath
                bytes = $artifactItem.Length
                sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $artifactPath).Hash
                eol_profile = 'UTF-8 LF-normalized, terminal LF retained'
            }
            dependencies = $dependencies
            cross_references = @()
            cross_reference_state = 'Not analyzed or inferred by coordinate-only canon control.'
            review_state = 'Exact tranche coordinates and retained-artifact identity replayed; target review remains outside this task.'
            uncertainty = $spec.uncertainty
            target_locator_state = 'lane_owned_not_collected_by_german_source_owner'
            indexing_limit = 'This record covers the declared tranche envelope; internal theorem, equation, note, and target structures were not silently inferred.'
        }
        Add-Record $rows $record
        $lastTranche = $recordId
    }
}

$defectPath = Join-Path (Join-Path $Root 'ledgers') 'DEFECT_INTAKE_ADJUDICATION.jsonl'
$defectSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $defectPath).Hash
$sequence++
$p22 = [ordered]@{
    schema = 'noeth.struct.v1'
    record_id = 'NOETH-STR-{0:D3}' -f $sequence
    object_type = 'editorial_locus'
    parent_unit_id = 'NOETH-P22'
    parent_binder_id = $null
    order = $sequence
    label = 'NOETH-DEF-P22-0001'
    authority = $authority
    source_ref = [ordered]@{
        path = 'ledgers/DEFECT_INTAKE_ADJUDICATION.jsonl'
        locator = 'NOETH-DEFREC-0037'
        sha256 = $defectSha
    }
    source_coordinates = [ordered]@{
        ed0002_line = 12840
        raw_line_range = '[1036032,1036137)'
        raw_line_bytes = 105
        raw_line_sha256 = 'F6C3D8FED48B32DC5EB8C5F6D5CAA7A989997E0E674775B29C684FEC9B5553C0'
        lf_line_range = '[1024112,1024217)'
        content_bytes = 104
        content_sha256 = '352B6CF53EF8296F705C7B132A5577A8A378610D51F02F8F7FB7955A0B420825'
        diplomatic_print_reading = '\Bmod_\lambda'
        published_parent_reading = '\Bmod_i'
        accepted_editorial_reading = '\Bmod_\lambda'
        printed_page = 57
        output_page = 228
    }
    retained_artifact = [ordered]@{
        path = 'evidence/NOETH-DEF-P22-0001/GDZ_P22_printed_p57_PPN235181684_0088_leaf61.jpg'
        bytes = 1277724
        sha256 = '32C0D0626784C504CD3AC0602720E2F4502A42A7A7ABF4DCB860FEF0AA024150'
        eol_profile = 'not applicable: binary JPEG primary witness'
    }
    dependencies = @('NOETH-DEFREC-0037', 'NOETH-DEC-20260804-005', 'NOETH-LIN-EDGE-005')
    cross_references = @('NOETH-DE-ED-0002', 'NOETH-DE-PUB-GITHUB-P02P49-20260719')
    cross_reference_state = 'Exact editorial and lineage cross-references recorded; no target cross-reference inferred.'
    review_state = 'Accepted later-transcription repair; two-pass build and focused page-228 QA complete; no independent human validation receipt.'
    uncertainty = 'Primary print was directly inspected and lambda is visible; corpus-wide critical-edition status is not claimed.'
    target_locator_state = 'lane_owned_not_collected_by_german_source_owner'
    indexing_limit = 'This record indexes only the repaired mathematical locus and its evidence, not the surrounding paper structure.'
}
Add-Record $rows $p22

$p25Path = Join-Path (Join-Path $Root 'receipts') 'P25_YEAR.json'
$p25Sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $p25Path).Hash
$sequence++
$p25 = [ordered]@{
    schema = 'noeth.struct.v1'
    record_id = 'NOETH-STR-{0:D3}' -f $sequence
    object_type = 'bibliography_locus'
    parent_unit_id = 'NOETH-P25'
    parent_binder_id = $null
    order = $sequence
    label = 'NOETH-P25-YEAR-20260804'
    authority = $authority
    source_ref = [ordered]@{
        path = 'receipts/P25_YEAR.json'
        locator = '/current_ed0001_locus'
        sha256 = $p25Sha
    }
    source_coordinates = [ordered]@{
        ed0002_line = 14149
        raw_line_range = '[1225132,1225171)'
        raw_line_bytes = 39
        raw_line_sha256 = 'C5F459A2E7CB3CB9ED278858248A8C18274C0097498AF31AA8EBEDB63E1B71C0'
        lf_line_range = '[1211904,1211942)'
        lf_line_bytes = 38
        lf_line_sha256 = 'E28B5D04D398641E51CEA228D7EF8B303991667B2583CDB6F84E8F01522D699E'
        content_bytes = 37
        content_sha256 = '4B92C8F1FEC18D2D1AEEAF1D10AF94470C94968BDE860828970A75B026D1BDD7'
        citation = 'J. Ber. d. DMV 33 (1924), S. 116--120'
        standard_article_or_nominal_volume_year = 1924
        bound_volume_imprint_and_GDZ_dateIssued = 1925
    }
    retained_artifact = [ordered]@{
        path = 'evidence/P25_year/title.jpg'
        bytes = 119153
        sha256 = 'E968B097A4E13EE03A5551048C2393E6AFF3699A103A479F16704E6DBAE14744'
        eol_profile = 'not applicable: binary JPEG primary witness'
    }
    dependencies = @('NOETH-DEFREC-0043', 'NOETH-DEC-20260804-017')
    cross_references = @('evidence/P25_year/mets.xml', 'evidence/P25_year/p116.jpg')
    cross_reference_state = 'Primary print, official catalog metadata, and bibliography evidence are distinguished by role.'
    review_state = 'Resolved as two different bibliographic facts; current ED0002 body preserves the inherited reading.'
    uncertainty = 'No independent human validation receipt; the primary print and official metadata were directly inspected.'
    target_locator_state = 'lane_owned_not_collected_by_german_source_owner'
    indexing_limit = 'This record indexes only the Paper-25 bibliography year locus, not the paper internal structure.'
}
Add-Record $rows $p25

$p08Path = Join-Path (Join-Path $Root 'receipts') 'P08_v2.json'
$p08Sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $p08Path).Hash
$sequence++
$p08 = [ordered]@{
    schema = 'noeth.struct.v1'
    record_id = 'NOETH-STR-{0:D3}' -f $sequence
    object_type = 'editorial_locus'
    parent_unit_id = 'NOETH-P08'
    parent_binder_id = 'NOETH-DE-BINDER-P08-ZH-COMPLETE-20260804-002'
    order = $sequence
    label = 'NOETH-DEF-P08-0001'
    authority = $authority
    source_ref = [ordered]@{
        path = 'receipts/P08_v2.json'
        locator = '/changed_locus'
        sha256 = $p08Sha
    }
    source_coordinates = [ordered]@{
        ed0002_line = 6042
        retained_line = 86
        raw_line_range = '[403237,403829)'
        raw_line_bytes = 592
        raw_line_sha256 = 'BB2D7D51EEF47815E88E73E7676F3FDA79BD42B1BE1FFC9F22F55904918796D2'
        retained_lf_range = '[8379,8971)'
        retained_lf_bytes = 592
        content_bytes = 591
        content_sha256 = '4597A61B82E3BA8A07418E2E6CFDF5CB3821A92C42D4BB92D6695DA2631719E7'
        diplomatic_print_reading = 'c_1,c_2'
        inherited_transcription_reading = '\\theta_1,\\theta_2'
        accepted_editorial_reading = 'c_1,c_2'
        printed_page = 96
        output_page = 96
    }
    retained_artifact = [ordered]@{
        path = 'evidence/P08_c1c2/page.jpg'
        bytes = 2121926
        sha256 = 'ABAEBA56F68D62865CACAB8EAC706028AAF0A73D8F78245AC4F4E01A574C94E6'
        eol_profile = 'not applicable: binary JPEG primary witness'
    }
    dependencies = @('NOETH-DEFREC-0044', 'NOETH-DEC-20260804-018', 'NOETH-LIN-EDGE-007', 'NOETH-DE-BINDER-P08-ZH-COMPLETE-20260804-002')
    cross_references = @('NOETH-DE-ED-0001', 'NOETH-DE-ED-0002')
    cross_reference_state = 'Primary print, inherited transcription, editorial repair, and replacement binder are distinguished by role.'
    review_state = 'Checker-confirmed later-transcription repair; schema validation, two-pass build, and focused output-page QA complete.'
    uncertainty = 'The printed variables are visually clear; this adjudication does not imply corpus-wide critical-edition status.'
    target_locator_state = 'lane_owned_not_collected_by_german_source_owner'
    indexing_limit = 'This record indexes only the repaired Paper-8 mathematical locus and its evidence.'
}
Add-Record $rows $p08

[IO.File]::WriteAllLines($outPath, $rows, [Text.UTF8Encoding]::new($false))
Write-Output "records=$($rows.Count)"
Write-Output "bytes=$((Get-Item -LiteralPath $outPath).Length)"
Write-Output "sha256=$((Get-FileHash -Algorithm SHA256 -LiteralPath $outPath).Hash)"
