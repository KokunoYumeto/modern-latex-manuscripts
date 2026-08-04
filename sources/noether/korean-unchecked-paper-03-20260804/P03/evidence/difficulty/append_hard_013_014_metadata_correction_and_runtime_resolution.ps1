$ErrorActionPreference = 'Stop'

$jsonlPath = Join-Path $PSScriptRoot 'difficulty_ledger.jsonl'
$csvPath = Join-Path $PSScriptRoot 'difficulty_ledger.csv'
$records = @(
    Get-Content -LiteralPath $jsonlPath -Encoding UTF8 |
        Where-Object { $_.Length -gt 0 }
)
$last = $records[-1] | ConvertFrom-Json
if (
    $records.Count -ne 12 -or
    $last.record_id -ne 'CJK-KO-P03-HARD-012' -or
    $last.record_sha256 -ne '53136065D0F516D3106C1FFEE299F93B493C097268174AF31BB9F91FC9D997CC'
) {
    throw 'Unexpected append cursor; refusing to mutate the append-only ledger.'
}

$authorityPath = '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/noether/07_german_canon_control/candidates/NOETH-DE-ED-0001/Noether_German_NOETH-DE-ED-0001.tex'
$authoritySha = 'D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB'
$initializerPath = '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/03_working_translations/noether_paper03_ko_translation_001_20260804/evidence/difficulty/initialize_difficulty_ledger.ps1'
$ledgerPath = '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/03_working_translations/noether_paper03_ko_translation_001_20260804/evidence/difficulty/difficulty_ledger.jsonl'
$frozenReportPath = '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/03_working_translations/noether_paper03_ko_translation_001_20260804/evidence/csv_artifact_validation/CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT_PRE_HARD013_20260804.json'
$validatorPath = '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/03_working_translations/noether_paper03_ko_translation_001_20260804/evidence/csv_artifact_validation/validate_csv_projections_artifact_tool.mjs'
$nodePath = '${PRIVATE_USER_ROOT}/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
$nodeModulesPath = '${PRIVATE_USER_ROOT}/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules'

function New-Authority {
    [ordered]@{
        path = $authorityPath
        snapshot_sha256 = $authoritySha
        historical_whole_source_sha256 = $authoritySha
        locators = @('P03 reproducibility metadata only; no source or target review')
        unit_slice_sha256 = [ordered]@{
            U01 = 'DF50EAD7065F663901F51ADFCA37A138921063362CA449665D37B855921B496C'
            U02 = 'A7B7CA981F7B8D6B32171BF0709E27440A25B2754642BD095304E54A5A25D5C6'
            U03 = '0D110465AEE20E18EE1427577D33D435FCF97D5CA99BEF3878EF52DC341F01A5'
        }
    }
}

function Add-Record {
    param(
        [Parameter(Mandatory)] [System.Collections.Specialized.OrderedDictionary] $Record,
        [Parameter(Mandatory)] [System.Collections.Specialized.OrderedDictionary] $CsvRow
    )
    $placeholder = $Record | ConvertTo-Json -Depth 20 -Compress
    $hash = [Convert]::ToHexString(
        [Security.Cryptography.SHA256]::HashData(
            [Text.Encoding]::UTF8.GetBytes($placeholder)
        )
    )
    $Record.record_sha256 = $hash
    $line = $Record | ConvertTo-Json -Depth 20 -Compress
    [IO.File]::AppendAllText(
        $jsonlPath,
        $line + [Environment]::NewLine,
        [Text.UTF8Encoding]::new($false)
    )
    $CsvRow.record_sha256 = $hash
    $csvLine = @([pscustomobject]$CsvRow | ConvertTo-Csv -NoTypeInformation)[1]
    [IO.File]::AppendAllText(
        $csvPath,
        $csvLine + [Environment]::NewLine,
        [Text.UTF8Encoding]::new($false)
    )
    return $hash
}

$record13 = [ordered]@{
    schema_version = '1.0.0'
    record_id = 'CJK-KO-P03-HARD-013'
    recorded_at = '2026-08-04'
    time_precision = 'day'
    append_sequence = 13
    previous_record_sha256 = $last.record_sha256
    work_id = 'NOE-P03-KO'
    unit_ids = @()
    authority = New-Authority
    targets = @()
    category = 'metadata_integrity_failure'
    sense_window = 'Append-only ledger semantic integrity versus syntactically valid JSON and CSV projections.'
    fact_classes = @('source_fact', 'computation')
    symptom = 'The immutable HARD-011 line was syntactically valid and chain-valid but several trailing semantic fields were mangled; the original validator did not enforce their documented enums.'
    cause_evidence = @(
        [ordered]@{
            kind = 'source_fact'
            detail = 'HARD-011 contains recurrence_cues=["s"], mandarin_simplified_dominance_risk="interpolation", lexical_attractor_basin="syntax. -RecurrenceCues @(JavaScript", related_decision_ids=["template"], related_structural_ids=["containing"], transferable_lesson="PowerShell", and revisit_condition="variable,nested".'
            path = $ledgerPath
            sha256 = 'CC6B3473799957FADEB7E50F41A8BD132C2AFB68BA838F657819E52D4C098C06'
        },
        [ordered]@{
            kind = 'source_fact'
            detail = 'The preserved initializer source gives the complete intended HARD-011 values and therefore provides recovery evidence without rewriting the old line.'
            path = $initializerPath
            sha256 = '5D650B210E4647318148627151783E1F550B4BCD6C3D736157F0482FC79EE826'
        },
        [ordered]@{
            kind = 'computation'
            detail = 'The first validator checked required fields, hashes, sequencing, and CSV identity but not schema enums; consequently it could return PASS for the malformed semantic values.'
            path = $null
            sha256 = $null
        }
    )
    attempted_approaches = @(
        [ordered]@{
            approach = 'Treat syntactic validity, hash-chain validity, and CSV identity as sufficient.'
            outcome = 'Rejected after final semantic inspection exposed the mangled fields.'
            status = 'failed'
        },
        [ordered]@{
            approach = 'Rewrite HARD-011 in place.'
            outcome = 'Rejected because corrections must append and preserve failed history.'
            status = 'rejected'
        },
        [ordered]@{
            approach = 'Append a full correction successor and strengthen validation while retaining the exact historical line.'
            outcome = 'Accepted.'
            status = 'accepted'
        }
    )
    rejected_approaches = @('Silent in-place repair', 'Suppress the malformed predecessor', 'Continue relying on syntax-only validation')
    resolution_state = 'resolved'
    resolution = 'This record corrects HARD-011 by append. Intended values are recurrence_cues=["JavaScript template containing PowerShell variable","nested interpolation syntax"], mandarin_simplified_dominance_risk="not_applicable", lexical_attractor_basin="not_applicable", related_decision_ids=[], related_structural_ids=["NOE-P03-KO-WORK-001"], transferable_lesson="When one language generates another, treat interpolation markers as evidence-bearing syntax and test before writing.", and revisit_condition="Recur if a future generated script embeds the braced interpolation of another language in JavaScript."'
    evidence = @(
        [ordered]@{
            kind = 'initializer_source'
            detail = 'Complete intended HARD-011 call retained in the initializer.'
            path = $initializerPath
            sha256 = '5D650B210E4647318148627151783E1F550B4BCD6C3D736157F0482FC79EE826'
        }
    )
    residual_risk = 'The immutable HARD-011 line remains a known malformed historical record; consumers must apply this correction successor or use the documented validator exception.'
    recurrence_cues = @('schema-valid JSON with semantically invalid enum values', 'validator checks hash chain but omits enum/domain checks', 'CSV projection faithfully reproduces malformed source data')
    mandarin_simplified_dominance_risk = 'not_applicable'
    lexical_attractor_basin = 'not_applicable'
    related_decision_ids = @()
    related_structural_ids = @('NOE-P03-KO-WORK-001')
    transferable_lesson = 'Validate domain semantics as well as JSON syntax, stable IDs, hashes, and flat-table identity; append a correction rather than hiding an already-recorded failure.'
    review_state = 'producer_metadata_unchecked'
    supersession_state = 'current'
    revisit_condition = 'Revisit if any downstream consumer ignores append corrections or treats HARD-011 as current semantic metadata.'
    record_sha256 = $null
}
$csv13 = [ordered]@{
    record_id = 'CJK-KO-P03-HARD-013'
    append_sequence = 13
    recorded_at = '2026-08-04'
    time_precision = 'day'
    category = 'metadata_integrity_failure'
    unit_ids = ''
    source_locators = 'P03 reproducibility metadata only; no source or target review'
    target_ids = ''
    resolution_state = 'resolved'
    symptom = $record13.symptom
    residual_risk = $record13.residual_risk
    recurrence_cues = 'schema-valid JSON with semantically invalid enum values;validator checks hash chain but omits enum/domain checks;CSV projection faithfully reproduces malformed source data'
    related_decision_ids = ''
    related_structural_ids = 'NOE-P03-KO-WORK-001'
    revisit_condition = $record13.revisit_condition
    record_sha256 = $null
}
$hash13 = Add-Record -Record $record13 -CsvRow $csv13

$record14 = [ordered]@{
    schema_version = '1.0.0'
    record_id = 'CJK-KO-P03-HARD-014'
    recorded_at = '2026-08-04'
    time_precision = 'day'
    append_sequence = 14
    previous_record_sha256 = $hash13
    work_id = 'NOE-P03-KO'
    unit_ids = @()
    authority = New-Authority
    targets = @()
    category = 'tooling_resolution'
    sense_window = 'Exact bundled Node and node_modules identities versus guessed or independently installed runtimes.'
    fact_classes = @('source_fact', 'computation')
    symptom = 'HARD-012 held the required artifact-tool CSV validation after two workspace-dependency locator stalls.'
    cause_evidence = @(
        [ordered]@{
            kind = 'source_fact'
            detail = "The exact supplied runtime is $nodePath (SHA-256 63C259C81E5D472B5F11C8D506070130CB04A1ECF84B80377A34ED6EC9048088); the exact dependency root is $nodeModulesPath."
            path = $nodePath
            sha256 = '63C259C81E5D472B5F11C8D506070130CB04A1ECF84B80377A34ED6EC9048088'
        },
        [ordered]@{
            kind = 'computation'
            detail = 'Using those exact paths through a temporary junction, @oai/artifact-tool imported all three CSV projections and returned PASS without rendering.'
            path = $frozenReportPath
            sha256 = 'EA0F81F536EA8D5FB031F2FCD59B76A9EDE9F6AF5D3EDF44B5BEEB7D29D1F35C'
        }
    )
    attempted_approaches = @(
        [ordered]@{
            approach = 'Use the supplied bundled runtime and dependency root exactly, with a temporary node_modules junction only for module resolution.'
            outcome = 'Accepted; artifact-tool validation passed.'
            status = 'accepted'
        },
        [ordered]@{
            approach = 'Render the imported CSV workbooks.'
            outcome = 'Rejected by the translation-only role boundary.'
            status = 'rejected'
        }
    )
    rejected_approaches = @('Guess a runtime path', 'Install alternate dependencies', 'Render or visually approve spreadsheet projections')
    resolution_state = 'resolved'
    resolution = 'HARD-012 is resolved by an exact runtime/dependency-path receipt and a frozen PASS artifact-tool report. The canonical report must be rerun after these append-only ledger rows change the difficulty CSV.'
    evidence = @(
        [ordered]@{
            kind = 'artifact_tool_report'
            detail = 'Frozen pre-HARD013 PASS validates structural, twelve-row difficulty, and zero-row visual CSV projections without rendering.'
            path = $frozenReportPath
            sha256 = 'EA0F81F536EA8D5FB031F2FCD59B76A9EDE9F6AF5D3EDF44B5BEEB7D29D1F35C'
        },
        [ordered]@{
            kind = 'validator_source'
            detail = 'Durable artifact-tool validator source copied into the producer evidence root.'
            path = $validatorPath
            sha256 = '4E34E4062E758649ABE62AE74176D1D0CFD1EBDDDBD0CBA782595DD1ADF9BFA3'
        }
    )
    residual_risk = 'Every CSV mutation requires a fresh canonical artifact-tool report; PASS is reproducibility evidence only, not Korean, formula, render, publication, or rights approval.'
    recurrence_cues = @('CSV projection hash changes', 'bundled runtime path changes', 'artifact-tool import or inspection error')
    mandarin_simplified_dominance_risk = 'not_applicable'
    lexical_attractor_basin = 'not_applicable'
    related_decision_ids = @()
    related_structural_ids = @('NOE-P03-KO-WORK-001')
    transferable_lesson = 'Freeze the first successful report that resolves a tooling hold, then rerun the canonical report after append-only metadata changes its own CSV projection.'
    review_state = 'producer_metadata_unchecked'
    supersession_state = 'current'
    revisit_condition = 'Rerun the durable artifact-tool validator after any structural, difficulty, or visual CSV byte change.'
    record_sha256 = $null
}
$csv14 = [ordered]@{
    record_id = 'CJK-KO-P03-HARD-014'
    append_sequence = 14
    recorded_at = '2026-08-04'
    time_precision = 'day'
    category = 'tooling_resolution'
    unit_ids = ''
    source_locators = 'P03 reproducibility metadata only; no source or target review'
    target_ids = ''
    resolution_state = 'resolved'
    symptom = $record14.symptom
    residual_risk = $record14.residual_risk
    recurrence_cues = 'CSV projection hash changes;bundled runtime path changes;artifact-tool import or inspection error'
    related_decision_ids = ''
    related_structural_ids = 'NOE-P03-KO-WORK-001'
    revisit_condition = $record14.revisit_condition
    record_sha256 = $null
}
$hash14 = Add-Record -Record $record14 -CsvRow $csv14

[pscustomobject]@{
    appended = @('CJK-KO-P03-HARD-013', 'CJK-KO-P03-HARD-014')
    hard_013_sha256 = $hash13
    hard_014_sha256 = $hash14
} | ConvertTo-Json
