$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$ledgerDir = $PSScriptRoot
$root = (Resolve-Path -LiteralPath (Join-Path $ledgerDir '..\..')).Path
$jsonlPath = Join-Path $ledgerDir 'DIFFICULTY_LEDGER.jsonl'
$csvPath = Join-Path $ledgerDir 'DIFFICULTY_LEDGER.csv'
$reportPath = Join-Path $ledgerDir 'DIFFICULTY_LEDGER_VALIDATION_REPORT.json'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$authorityContext = [ordered]@{
    pointer_id = 'NOETH-DE-AUTH-v003-20260804'
    pointer_sha256 = '932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197'
    authority_path = '${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\noether\07_german_canon_control\candidates\NOETH-DE-ED-0001\Noether_German_NOETH-DE-ED-0001.tex'
    authority_sha256 = 'D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB'
}
$targetPath = [ordered]@{
    U01 = Join-Path $root 'targets\Noether_P05_Korean_U01_UNCHECKED.tex'
    U02 = Join-Path $root 'targets\Noether_P05_Korean_U02_UNCHECKED.tex'
    U03 = Join-Path $root 'targets\Noether_P05_Korean_U03_UNCHECKED.tex'
    U04 = Join-Path $root 'targets\Noether_P05_Korean_U04_UNCHECKED.tex'
}
$targetHash = [ordered]@{
    U01 = 'EEB39C3A693410823F66A75BCE7DBB9906F35637BFFF87A55CE4A7B873A6F203'
    U02 = '62D644153874FFE07C839102D5EF222BCED55F693C1BA6E8E9FF318A670F8DEA'
    U03 = '2B7ADD81855DD9D06A1D2D17249F32F5D7BBDB458F7474E0BB7BC3F14A5FFA89'
    U04 = '8A50F7549C23A50A6A824C97763941535D12061EE08E32D2EC1D3F678FE4CA6B'
}
$structuralBuilder = Join-Path $root 'evidence\structural_index\build_and_validate_structural_index.ps1'
$structuralReport = Join-Path $root 'evidence\structural_index\PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json'

function Get-FileSha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Get-TextSha256([string]$Text) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([System.BitConverter]::ToString($sha.ComputeHash($utf8NoBom.GetBytes($Text)))).Replace('-', '')
    }
    finally {
        $sha.Dispose()
    }
}

function New-TargetArtifact([string]$Path, [AllowNull()][string]$Sha256) {
    return [ordered]@{ path = $Path; sha256 = $Sha256 }
}

function New-Evidence([string]$Kind, [AllowNull()][string]$Path, [AllowNull()][string]$Sha256, [string]$Result) {
    return [ordered]@{ kind = $Kind; path = $Path; sha256 = $Sha256; result = $Result }
}

$specs = @(
    [ordered]@{
        record_id = 'CJK-KO-P05-HARD-001'
        sequence = 1
        observed_at = $null
        time_precision = 'sequence_only'
        unit_ids = @()
        source_locators = @('Paper 5 pre-write hash-helper step; exact command timestamp unavailable')
        target_artifacts = @()
        state = 'resolved'
        symptom = 'The first hash-helper attempt used H, which PowerShell resolved to Get-History instead of the intended hashing helper.'
        cause_evidence = 'Command resolution selected the built-in H alias for Get-History. The failed output and exact command bytes were not retained; this limitation is explicit.'
        attempts = @(
            [ordered]@{ approach = 'Invoke the shorthand H as a hash helper.'; outcome = 'PowerShell executed Get-History; the intended hash computation did not occur.'; rejection_reason = 'Ambiguous shorthand collided with a built-in alias.' },
            [ordered]@{ approach = 'Repeat the exact failed command.'; outcome = 'Not attempted.'; rejection_reason = 'The routing directive explicitly required preserving the failure without redoing the command.' }
        )
        resolution_or_hold = 'Subsequent producer computations used explicit Get-FileHash and fully qualified .NET SHA-256 operations. The original failed command remains unreplayed metadata debt.'
        evidence = @((New-Evidence 'reported_tool_failure' $null $null 'H resolved to PowerShell Get-History; no failed-output artifact or hash exists.'))
        residual_risk = 'Other short aliases or implicit command names can silently resolve to unrelated PowerShell commands.'
        recurrence_cues = @('Single-letter helper invocation', 'Alias expansion', 'Hash output unexpectedly resembles command history')
        related_structural_ids = @('NOE-P05-KO-WORK-001')
        related_decision_ids = @()
        transferable_lesson = 'Use explicit command names for evidence hashing and preserve the first failed outcome without manufacturing a replay.'
        classification = 'computation'
    },
    [ordered]@{
        record_id = 'CJK-KO-P05-HARD-002'
        sequence = 2
        observed_at = '2026-08-04'
        time_precision = 'day'
        unit_ids = @('U01', 'U02', 'U03', 'U04')
        source_locators = @('Metadata-only structural builder patch before file creation')
        target_artifacts = @()
        state = 'resolved'
        symptom = 'The first structural-builder apply_patch orchestration failed before writing a file with ReferenceError: unit is not defined.'
        cause_evidence = 'A PowerShell braced unit-variable expression inside a JavaScript String.raw template was interpreted as JavaScript template interpolation.'
        attempts = @(
            [ordered]@{ approach = 'Embed PowerShell braced variable syntax directly in a JavaScript raw template.'; outcome = 'The JavaScript evaluator raised ReferenceError before apply_patch ran; no structural script or target bytes were written.'; rejection_reason = 'Cross-language interpolation made the patch payload ambiguous.' },
            [ordered]@{ approach = 'Replace braced interpolation with PowerShell string concatenation.'; outcome = 'The patch wrote the builder, and the builder subsequently validated 41 structural records.'; rejection_reason = $null }
        )
        resolution_or_hold = 'PowerShell diagnostic strings concatenate the unit name, avoiding JavaScript template interpolation.'
        evidence = @(
            (New-Evidence 'repaired_builder' $structuralBuilder 'AD4A6880CC2E02555A29385DC80DABA2F8D4398CD1AA8BEAA71222D9F54CD9C6' 'Current builder after repair.'),
            (New-Evidence 'validation_report' $structuralReport '77311B85095CC38E58F463D06B0554E6FDFFB98B99F97BC7A34C73417F6348E2' 'PASS with 41 unique structural records and no errors.')
        )
        residual_risk = 'Future mixed JavaScript and PowerShell patches can repeat the collision when braced variables occur in a JavaScript template.'
        recurrence_cues = @('String.raw template containing PowerShell braced variables', 'JavaScript ReferenceError before apply_patch output')
        related_structural_ids = @('NOE-P05-KO-WORK-001')
        related_decision_ids = @()
        transferable_lesson = 'Treat nested interpolation syntaxes as data-boundary hazards; use concatenation or an explicit placeholder layer.'
        classification = 'computation'
    },
    [ordered]@{
        record_id = 'CJK-KO-P05-HARD-003'
        sequence = 3
        observed_at = '2026-08-04'
        time_precision = 'day'
        unit_ids = @()
        source_locators = @('First difficulty-ledger builder apply_patch attempt before file creation')
        target_artifacts = @()
        state = 'resolved'
        symptom = 'The first difficulty-ledger builder patch failed before writing a file with JavaScript SyntaxError: Unexpected token right brace.'
        cause_evidence = 'The prose that attempted to document the structural failure repeated the literal nested braced-variable syntax inside the JavaScript raw template.'
        attempts = @(
            [ordered]@{ approach = 'Describe the prior interpolation failure using its literal braced syntax inside another raw template.'; outcome = 'The JavaScript parser rejected the patch before apply_patch ran.'; rejection_reason = 'The failure description reproduced the same executable delimiter pattern.' },
            [ordered]@{ approach = 'Describe the syntax in plain words without a literal interpolation token.'; outcome = 'The follow-up patch wrote the difficulty builder.'; rejection_reason = $null }
        )
        resolution_or_hold = 'Failure documentation now names the braced-variable pattern in prose without embedding its executable character sequence.'
        evidence = @((New-Evidence 'orchestration_failure' $null $null 'SyntaxError occurred before file creation; no failed builder artifact exists.'))
        residual_risk = 'Reproduction text can itself reactivate the syntax being documented.'
        recurrence_cues = @('Failure report contains live delimiter syntax', 'Parser error occurs before apply_patch output')
        related_structural_ids = @('NOE-P05-KO-WORK-001')
        related_decision_ids = @()
        transferable_lesson = 'When documenting an injection or interpolation failure, neutralize the triggering delimiter instead of reproducing it verbatim in an executable transport.'
        classification = 'computation'
    },
    [ordered]@{
        record_id = 'CJK-KO-P05-HARD-004'
        sequence = 4
        observed_at = '2026-08-04'
        time_precision = 'day'
        unit_ids = @('U02', 'U03', 'U04')
        source_locators = @('Whole lines 4547--4572; terms Zahlkörper, Gattungsbereich, affektlos, Integritätsbasis, ganze rationale Verbindung, relativ ganze Funktionen, Resultante')
        target_artifacts = @(
            (New-TargetArtifact $targetPath.U02 $targetHash.U02),
            (New-TargetArtifact $targetPath.U03 $targetHash.U03),
            (New-TargetArtifact $targetPath.U04 $targetHash.U04)
        )
        state = 'held'
        symptom = 'Several Hilbert-era terms have multiple plausible modern Korean attractors whose present-day senses do not align cleanly with the source windows.'
        cause_evidence = 'Zahlkörper is explicitly broad enough to include all complex numbers; Integritätsbasis is defined through polynomial elements; Gattungsbereich and affektlos lack established Korean evidence in this producer pass.'
        attempts = @(
            [ordered]@{ approach = 'Choose concise Hangul-first Korean forms while retaining German witnesses for the two least stable terms.'; outcome = 'Producer draft uses 수체, 라그랑주 종영역(Gattungsbereich), 아펙트 없는(affektlos) 방정식, 정수성 기저, and 종결식.'; rejection_reason = $null },
            [ordered]@{ approach = 'Treat Sino-xenic resemblance or Mandarin terminology as Korean evidence.'; outcome = 'Rejected without use.'; rejection_reason = 'Chinese does not authorize Korean and the evidence shelf has Mandarin-Simplified dominance debt.' }
        )
        resolution_or_hold = 'All forms remain explicit independent-checker holds with source sense windows and alternatives in TRANSLATION_CHOICES_U01_U04.md.'
        evidence = @((New-Evidence 'producer_choice_ledger' (Join-Path $root 'TRANSLATION_CHOICES_U01_U04.md') $null 'Sense windows, alternatives, lexical-attractor basins, and adverse evidence recorded.'))
        residual_risk = 'A fluent-looking calque may conceal the wrong historical algebraic meaning.'
        recurrence_cues = @('Historical ganze or Integrität terminology', 'German term lacks a stable Korean corpus witness', 'Broad historical Zahlkörper usage')
        related_structural_ids = @('NOE-P05-KO-U02-DEFINITION-001', 'NOE-P05-KO-U03-DEFINITION-001', 'NOE-P05-KO-U04-STATEMENT-001')
        related_decision_ids = @()
        transferable_lesson = 'Bind terminology to an explicit local sense window and retain adverse evidence instead of optimizing for cross-language familiarity.'
        classification = 'editorial_inference'
    },
    [ordered]@{
        record_id = 'CJK-KO-P05-HARD-005'
        sequence = 5
        observed_at = '2026-08-04'
        time_precision = 'day'
        unit_ids = @('U01', 'U02', 'U03', 'U04')
        source_locators = @('All Paper 5 translated prose; whole lines 4535--4572')
        target_artifacts = @(
            (New-TargetArtifact $targetPath.U01 $targetHash.U01),
            (New-TargetArtifact $targetPath.U02 $targetHash.U02),
            (New-TargetArtifact $targetPath.U03 $targetHash.U03),
            (New-TargetArtifact $targetPath.U04 $targetHash.U04)
        )
        state = 'active_control'
        symptom = 'Hangul/Hanja policy, ko-KR versus ko-KP adaptation, and Mandarin-Simplified dominance can create false readiness even when the producer Korean reads smoothly.'
        cause_evidence = 'No independent Korean reviewer or local evidence corpus was applied. Cross-CJK resemblance is not language-specific validation.'
        attempts = @(
            [ordered]@{ approach = 'Use provisional Hangul-first ko-KR prose and record Hanja and ko-KP decisions as holds.'; outcome = 'Targets remain readable producer drafts while jurisdictional and script-policy claims remain unmade.'; rejection_reason = $null },
            [ordered]@{ approach = 'Infer Hanja, ko-KP, or Korean readiness from Chinese forms.'; outcome = 'Rejected without use.'; rejection_reason = 'Language authority is non-transferable.' }
        )
        resolution_or_hold = 'Independent Korean checking must decide local evidence, first-use Hanja, spelling, spacing, and any separate ko-KP adaptation.'
        evidence = @((New-Evidence 'checker_handoff' (Join-Path $root 'CHECKER_HANDOFF_U01_U04.md') $null 'Explicit local-evidence, Hanja, ko-KR, and ko-KP return requested.'))
        residual_risk = 'Unreviewed Hangul terminology may encode a Mandarin-dominant calque or a South-only standard.'
        recurrence_cues = @('Sino-xenic term appears self-evident', 'No Korean citation', 'Request to treat one Korean standard as universal')
        related_structural_ids = @('NOE-P05-KO-WORK-001')
        related_decision_ids = @()
        transferable_lesson = 'Keep dominance debt qualitative and blocking; script and regional-standard decisions require their own evidence.'
        classification = 'model_preference'
    },
    [ordered]@{
        record_id = 'CJK-KO-P05-HARD-006'
        sequence = 6
        observed_at = '2026-08-04'
        time_precision = 'day'
        unit_ids = @('U01', 'U02', 'U03', 'U04')
        source_locators = @('Routed source slices 4535--4545, 4547--4557, 4559--4563, and 4565--4572')
        target_artifacts = @(
            (New-TargetArtifact $targetPath.U01 $targetHash.U01),
            (New-TargetArtifact $targetPath.U02 $targetHash.U02),
            (New-TargetArtifact $targetPath.U03 $targetHash.U03),
            (New-TargetArtifact $targetPath.U04 $targetHash.U04)
        )
        state = 'resolved'
        symptom = 'A prior production unit showed that ordinary JavaScript strings can consume TeX backslashes, so Paper 5 had a recurrence risk before metadata freeze.'
        cause_evidence = 'Nested JavaScript escaping can alter TeX control sequences even when the intended patch text looks correct.'
        attempts = @(
            [ordered]@{ approach = 'Write all four Paper 5 targets with String.raw apply_patch payloads.'; outcome = 'No control-sequence inventory differences were found between each source slice and target body.'; rejection_reason = $null },
            [ordered]@{ approach = 'Compile or semantically inspect formulas to prove correctness.'; outcome = 'Not attempted.'; rejection_reason = 'The producer lane is translation-only and compilation, formula review, and rendering are prohibited.' }
        )
        resolution_or_hold = 'Raw-string writes plus a mechanical control-token multiset, dollar parity, and display-delimiter count were used. These establish write integrity only.'
        evidence = @((New-Evidence 'mechanical_write_integrity' $null $null 'U01--U04 source/target TeX control-sequence multisets matched; dollar counts were even; U04 display delimiters were 1/1.'))
        residual_risk = 'Matching token inventories do not prove formula placement, semantics, source correctness, or Korean correctness.'
        recurrence_cues = @('Ordinary JavaScript string contains TeX backslashes', 'Literal parentheses appear where TeX inline delimiters were intended')
        related_structural_ids = @('NOE-P05-KO-U04-DISPLAY-001')
        related_decision_ids = @()
        transferable_lesson = 'Separate byte-integrity checks from mathematical review and never upgrade a token-count PASS into a correctness claim.'
        classification = 'computation'
    }
)

$records = [System.Collections.Generic.List[object]]::new()
$previousHash = $null
foreach ($spec in $specs) {
    $base = [ordered]@{
        schema_version = '1.0'
        record_id = $spec.record_id
        sequence = $spec.sequence
        observed_at = $spec.observed_at
        time_precision = $spec.time_precision
        work_id = 'NOE-P05'
        unit_ids = @($spec.unit_ids)
        authority_context = $authorityContext
        source_locators = @($spec.source_locators)
        target_artifacts = @($spec.target_artifacts)
        state = $spec.state
        symptom = $spec.symptom
        cause_evidence = $spec.cause_evidence
        attempts = @($spec.attempts)
        resolution_or_hold = $spec.resolution_or_hold
        evidence = @($spec.evidence)
        residual_risk = $spec.residual_risk
        recurrence_cues = @($spec.recurrence_cues)
        related_structural_ids = @($spec.related_structural_ids)
        related_decision_ids = @($spec.related_decision_ids)
        transferable_lesson = $spec.transferable_lesson
        classification = $spec.classification
        previous_record_sha256 = $previousHash
    }
    $base.record_sha256 = Get-TextSha256 ($base | ConvertTo-Json -Compress -Depth 16)
    $record = [pscustomobject]$base
    $records.Add($record)
    $previousHash = $record.record_sha256
}

$errors = [System.Collections.Generic.List[string]]::new()
$candidateLines = @($records | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 16 })
if (Test-Path -LiteralPath $jsonlPath) {
    $existingLines = @([System.IO.File]::ReadAllLines($jsonlPath, $utf8NoBom) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    if ($existingLines.Count -gt $candidateLines.Count) {
        $errors.Add('append-only violation: existing ledger is longer than candidate ledger')
    }
    else {
        for ($index = 0; $index -lt $existingLines.Count; $index++) {
            if ($existingLines[$index] -ne $candidateLines[$index]) {
                $errors.Add("append-only prefix mismatch at line $($index + 1)")
            }
        }
    }
}
if ($errors.Count -eq 0) {
    [System.IO.File]::WriteAllLines($jsonlPath, $candidateLines, $utf8NoBom)
}

$ids = @($records.record_id)
if (($ids | Sort-Object -Unique).Count -ne $records.Count) {
    $errors.Add('duplicate record_id')
}
$expectedPrevious = $null
foreach ($record in $records) {
    if ($record.previous_record_sha256 -ne $expectedPrevious) {
        $errors.Add("hash-chain predecessor mismatch for $($record.record_id)")
    }
    foreach ($artifact in $record.target_artifacts) {
        if ($artifact.sha256 -and (Test-Path -LiteralPath $artifact.path)) {
            if ((Get-FileSha256 $artifact.path) -ne $artifact.sha256) {
                $errors.Add("target artifact mismatch for $($record.record_id): $($artifact.path)")
            }
        }
    }
    $expectedPrevious = $record.record_sha256
}

$written = @([System.IO.File]::ReadAllLines($jsonlPath, $utf8NoBom) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
foreach ($line in $written) {
    $parsed = $line | ConvertFrom-Json -Depth 30
    $baseLine = $line -replace ',"record_sha256":"[A-F0-9]{64}"}$', '}'
    if ((Get-TextSha256 $baseLine) -ne $parsed.record_sha256) {
        $errors.Add("record self-hash mismatch for $($parsed.record_id)")
    }
}

$csvRows = $records | ForEach-Object {
    [pscustomobject]@{
        record_id = $_.record_id
        sequence = $_.sequence
        observed_at = $_.observed_at
        time_precision = $_.time_precision
        work_id = $_.work_id
        unit_ids_json = ($_.unit_ids | ConvertTo-Json -Compress)
        state = $_.state
        symptom = $_.symptom
        cause_evidence = $_.cause_evidence
        attempts_json = ($_.attempts | ConvertTo-Json -Compress -Depth 8)
        resolution_or_hold = $_.resolution_or_hold
        evidence_json = ($_.evidence | ConvertTo-Json -Compress -Depth 8)
        residual_risk = $_.residual_risk
        recurrence_cues_json = ($_.recurrence_cues | ConvertTo-Json -Compress)
        related_structural_ids_json = ($_.related_structural_ids | ConvertTo-Json -Compress)
        related_decision_ids_json = ($_.related_decision_ids | ConvertTo-Json -Compress)
        transferable_lesson = $_.transferable_lesson
        classification = $_.classification
        previous_record_sha256 = $_.previous_record_sha256
        record_sha256 = $_.record_sha256
    }
}
$csvRows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8
$csvReplay = @(Import-Csv -LiteralPath $csvPath)
if ($csvReplay.Count -ne $records.Count) {
    $errors.Add("CSV count mismatch: expected $($records.Count) got $($csvReplay.Count)")
}

$stateCounts = [ordered]@{}
foreach ($group in ($records | Group-Object state | Sort-Object Name)) {
    $stateCounts[$group.Name] = $group.Count
}
$report = [ordered]@{
    schema = 'DIFFICULTY_LEDGER.schema.json'
    builder_validator = 'build_and_validate_difficulty_ledger.ps1'
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    append_only_prefix_verified = ($errors.Count -eq 0)
    record_count = $records.Count
    unique_record_count = ($ids | Sort-Object -Unique).Count
    latest_record_id = $records[-1].record_id
    chain_head_sha256 = $records[-1].record_sha256
    state_counts = $stateCounts
    jsonl_sha256 = if (Test-Path -LiteralPath $jsonlPath) { Get-FileSha256 $jsonlPath } else { $null }
    csv_sha256 = Get-FileSha256 $csvPath
    errors = @($errors)
    continuation_cursor = 'Independent Korean checker; append corrections and later failures without rewriting prior records.'
    scope_note = 'Producer difficulty and failure history. Resolved records remain in the chain; no record is a review or certification claim.'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 10), $utf8NoBom)
if ($errors.Count -gt 0) {
    throw "Difficulty-ledger validation failed: $($errors -join '; ')"
}
Write-Output ($report | ConvertTo-Json -Compress -Depth 10)
