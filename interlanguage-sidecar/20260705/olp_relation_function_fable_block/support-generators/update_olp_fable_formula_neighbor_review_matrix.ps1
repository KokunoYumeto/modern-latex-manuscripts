param(
    [string]$PackageRoot = "interlanguage-sidecar/20260705/olp_relation_function_fable_block"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$pkg = (Resolve-Path $PackageRoot).Path
$generated = Join-Path $pkg "generated-draft"
$supportGenerators = Join-Path $pkg "support-generators"
New-Item -ItemType Directory -Force -Path $generated, $supportGenerators | Out-Null

if ($PSCommandPath) {
    Copy-Item -LiteralPath $PSCommandPath -Destination (Join-Path $supportGenerators "update_olp_fable_formula_neighbor_review_matrix.ps1") -Force
}

function Import-ByKey {
    param(
        [string]$Path,
        [string]$Key
    )
    $map = @{}
    foreach ($row in (Import-Csv -LiteralPath $Path)) {
        $map[[string]$row.$Key] = $row
    }
    return $map
}

function Escape-Md {
    param([string]$Text)
    if ($null -eq $Text) { return "" }
    return ($Text -replace '\|','\|') -replace "`r?`n", " "
}

function Split-LexemeIds {
    param([string]$Text)
    if ([string]::IsNullOrWhiteSpace($Text)) { return @() }
    return @($Text -split ';' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
}

$scaffolds = @(Import-Csv -LiteralPath (Join-Path $pkg "pretranslation_scaffolds.csv"))
$branchQueue = Import-ByKey -Path (Join-Path $pkg "branch_gap_recovery_queue.csv") -Key "lexeme_id"
$branchWeights = Import-ByKey -Path (Join-Path $pkg "branch_weight_ledger.csv") -Key "lexeme_id"
$contexts = @(Import-Csv -LiteralPath (Join-Path $pkg "external_wikimedia_context_counts.csv"))
$forms = @(Import-Csv -LiteralPath (Join-Path $pkg "external_wikimedia_source_form_candidates.csv"))
$falseSlots = @(Import-Csv -LiteralPath (Join-Path $pkg "external_wikimedia_false_friend_review_slots.csv"))

$contextByLexeme = @{}
foreach ($ctx in $contexts) {
    foreach ($lex in (Split-LexemeIds $ctx.lexeme_ids)) {
        if (-not $contextByLexeme.ContainsKey($lex)) {
            $contextByLexeme[$lex] = [System.Collections.Generic.List[object]]::new()
        }
        $contextByLexeme[$lex].Add($ctx)
    }
}

$formsByLexeme = @{}
foreach ($form in $forms) {
    $lex = [string]$form.lexeme_id
    if (-not $formsByLexeme.ContainsKey($lex)) {
        $formsByLexeme[$lex] = [System.Collections.Generic.List[object]]::new()
    }
    $formsByLexeme[$lex].Add($form)
}

$falseByLexeme = @{}
foreach ($slot in $falseSlots) {
    $lex = [string]$slot.lexeme_id
    if (-not $falseByLexeme.ContainsKey($lex)) {
        $falseByLexeme[$lex] = [System.Collections.Generic.List[object]]::new()
    }
    $falseByLexeme[$lex].Add($slot)
}

$rows = [System.Collections.Generic.List[object]]::new()
foreach ($scaffold in $scaffolds) {
    $lex = [string]$scaffold.lexeme_id
    $queue = $branchQueue[$lex]
    $weight = $branchWeights[$lex]
    $ctxRows = @()
    if ($contextByLexeme.ContainsKey($lex)) { $ctxRows = @($contextByLexeme[$lex]) }
    $formRows = @()
    if ($formsByLexeme.ContainsKey($lex)) { $formRows = @($formsByLexeme[$lex]) }
    $slotRows = @()
    if ($falseByLexeme.ContainsKey($lex)) { $slotRows = @($falseByLexeme[$lex]) }

    $leadTotal = 0
    $formulaTotal = 0
    $emittedTotal = 0
    foreach ($ctx in $ctxRows) {
        $leadTotal += [int]$ctx.lead_contexts
        $formulaTotal += [int]$ctx.formula_contexts
        $emittedTotal += [int]$ctx.emitted_contexts
    }

    $sourceDocs = @($ctxRows | Select-Object -First 5 | ForEach-Object {
        "{0} [{1}; {2}]" -f $_.doc_id, $_.language, $_.branch
    })
    $formSummary = @($formRows | Select-Object -First 8 | ForEach-Object {
        "{0}:{1} ({2})" -f $_.language, $_.source_form, $_.source_document
    })

    $missingBranches = [string]$queue.missing_active_branches
    $nextAction = if ([string]::IsNullOrWhiteSpace($queue.next_source_canon_targets)) {
        "Owner lanes may draft from current source-probe baseline; still require direct source/reviewer verification before promotion."
    } else {
        $queue.next_source_canon_targets
    }

    $reviewFocus = if ([string]::IsNullOrWhiteSpace($missingBranches)) {
        "Formula-neighbor and register review; no branch-gap escalation from this OLP support row."
    } else {
        "Formula-neighbor review plus source-canon recovery for missing branch axis: $missingBranches."
    }

    $falsePrompt = if ($slotRows.Count -gt 0) {
        "Use external_wikimedia_false_friend_review_slots.csv; $($slotRows.Count) review slot(s) tied to recovered source-form candidates."
    } else {
        "No external false-friend slot emitted for this lexeme; keep general adverse-evidence guard."
    }

    $rows.Add([pscustomobject]@{
        lexeme_id = $lex
        gloss = $scaffold.gloss
        source_spine = $scaffold.source_spine
        formula_neighboring_usage_note = $scaffold.formula_neighboring_usage_note
        generated_interlanguage_control = $scaffold.generated_interlanguage_control
        english_control = $scaffold.english_control
        active_branch_count = $queue.active_branch_count
        effective_branch_number_D = $weight.effective_branch_number_D
        marginal_score = ""
        current_positive_branches = $queue.current_positive_branches
        missing_active_branches = $missingBranches
        external_context_documents = $ctxRows.Count
        external_lead_contexts = $leadTotal
        external_formula_contexts = $formulaTotal
        external_emitted_contexts = $emittedTotal
        external_source_documents = ($sourceDocs -join "; ")
        external_source_forms = ($formSummary -join "; ")
        branch_metric_status = $scaffold.branch_metric_status
        owner_route = $scaffold.owner_route
        review_focus = $reviewFocus
        false_friend_review_prompt = $falsePrompt
        next_source_or_owner_action = $nextAction
        source_use_label = "generated-draft/non-canonical formula-neighbor review matrix"
        claim_boundary = "support-only; no native review; no accepted terminology; no approval; no license clearance; no source certification; no final status; no translation completion"
    }) | Out-Null
}

$matrixCsv = Join-Path $generated "relation_function_formula_neighbor_review_matrix.csv"
$matrixJsonl = Join-Path $generated "relation_function_formula_neighbor_review_matrix.jsonl"
$matrixMd = Join-Path $generated "relation_function_formula_neighbor_review_matrix.md"
$summaryCsv = Join-Path $generated "relation_function_formula_neighbor_review_summary.csv"

$rows | Export-Csv -LiteralPath $matrixCsv -NoTypeInformation -Encoding UTF8

$jsonLines = foreach ($row in $rows) {
    $row | ConvertTo-Json -Compress -Depth 8
}
Set-Content -LiteralPath $matrixJsonl -Encoding UTF8 -Value $jsonLines

$readyRows = @($rows | Where-Object { [string]::IsNullOrWhiteSpace($_.missing_active_branches) })
$gapRows = @($rows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.missing_active_branches) })
$formulaContextTotal = ($rows | Measure-Object -Property external_formula_contexts -Sum).Sum
$emittedContextTotal = ($rows | Measure-Object -Property external_emitted_contexts -Sum).Sum

$summary = @(
    [pscustomobject]@{metric="matrix_rows"; value=$rows.Count; note="One row per relation/function lexeme in pretranslation_scaffolds.csv"},
    [pscustomobject]@{metric="rows_without_missing_branch_axis"; value=$readyRows.Count; note="Still generated-draft and non-canonical"},
    [pscustomobject]@{metric="rows_with_missing_branch_axis"; value=$gapRows.Count; note="Scoped draft may proceed, but source-canon recovery target remains recorded"},
    [pscustomobject]@{metric="external_formula_contexts_linked"; value=$formulaContextTotal; note="From external_wikimedia_context_counts.csv"},
    [pscustomobject]@{metric="external_context_windows_linked"; value=$emittedContextTotal; note="Lead plus formula-neighboring contexts"}
)
$summary | Export-Csv -LiteralPath $summaryCsv -NoTypeInformation -Encoding UTF8

$md = [System.Collections.Generic.List[string]]::new()
$md.Add("# Relation/Function Formula-Neighbor Review Matrix")
$md.Add("")
$md.Add("Status: generated-draft / non-canonical support only.")
$md.Add("")
$md.Add("This matrix binds relation/function pretranslation scaffold rows to branch weights, recovered external source-form candidates, formula-neighbor context counts, false-friend review slots, and owner next actions. It is support infrastructure for language owners and B3 packaging; it is not reviewer return, native review, accepted terminology, approval, source certification, license clearance, final status, or translation completion.")
$md.Add("")
$md.Add("## Counts")
$md.Add("")
foreach ($s in $summary) {
    $md.Add("- $($s.metric): $($s.value) -- $($s.note)")
}
$md.Add("")
$md.Add("## Review Rows")
$md.Add("")
$md.Add("| Lexeme | Branches | Missing Axis | Formula Contexts | Source Forms | Review Focus |")
$md.Add("| --- | ---: | --- | ---: | --- | --- |")
foreach ($row in $rows) {
    $sourceForms = if ([string]::IsNullOrWhiteSpace($row.external_source_forms)) { "none in external form candidates" } else { $row.external_source_forms }
    $cells = @(
        (Escape-Md $row.lexeme_id),
        (Escape-Md $row.active_branch_count),
        (Escape-Md $row.missing_active_branches),
        (Escape-Md ([string]$row.external_formula_contexts)),
        (Escape-Md $sourceForms),
        (Escape-Md $row.review_focus)
    )
    $md.Add("| " + ($cells -join " | ") + " |")
}
$md.Add("")
$md.Add("## Boundary")
$md.Add("")
$md.Add("All rows remain source-gated generated-draft support. Blank slots and review templates are not reviewer returns, mapping evidence, translation evidence, native review, accepted terminology, or approval.")
Set-Content -LiteralPath $matrixMd -Encoding UTF8 -Value $md

$packageLog = Join-Path $pkg "SESSION_LOGBOOK_20260705.md"
Add-Content -LiteralPath $packageLog -Encoding UTF8 -Value ""
Add-Content -LiteralPath $packageLog -Encoding UTF8 -Value "Formula-neighbor review matrix addendum: generated relation_function_formula_neighbor_review_matrix.csv/jsonl/md and relation_function_formula_neighbor_review_summary.csv under generated-draft/. Rows are source-gated generated-draft support only and do not alter mapping, translation, approval, native review, accepted terminology, source certification, license clearance, final status, or translation-completion counts."

$manifestPath = Join-Path $pkg "MANIFEST.csv"
$shaPath = Join-Path $pkg "SHA256SUMS.txt"
$payloadFiles = @(Get-ChildItem -LiteralPath $pkg -Recurse -File | Where-Object { $_.Name -notin @("MANIFEST.csv","SHA256SUMS.txt") } | Sort-Object FullName)
$manifestRows = foreach ($file in $payloadFiles) {
    $rel = [IO.Path]::GetRelativePath($pkg, $file.FullName).Replace('\','/')
    $label = if ($rel -like "source_bodies/*") {
        "source-body"
    } elseif ($rel -like "source_witnesses/*") {
        "source-witness"
    } elseif ($rel -like "generated-draft/*") {
        "generated-draft"
    } elseif ($rel -like "support-generators/*") {
        "support-generator"
    } elseif ($rel -like "*.md" -or $rel -like "*.csv" -or $rel -like "*.json" -or $rel -like "*.jsonl") {
        "audit-ledger"
    } else {
        "package-file"
    }
    [pscustomobject]@{
        relative_path = $rel
        bytes = $file.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $file.FullName).Hash.ToLowerInvariant()
        source_use_label = $label
        note = "Fable OLP relation/function block; no approval or completion claim"
    }
}
$manifestRows | Export-Csv -LiteralPath $manifestPath -NoTypeInformation -Encoding UTF8

$shaFiles = @(Get-ChildItem -LiteralPath $pkg -Recurse -File | Where-Object { $_.Name -ne "SHA256SUMS.txt" } | Sort-Object FullName)
$shaLines = foreach ($file in $shaFiles) {
    $rel = [IO.Path]::GetRelativePath($pkg, $file.FullName).Replace('\','/')
    "{0}  {1}" -f (Get-FileHash -Algorithm SHA256 -LiteralPath $file.FullName).Hash.ToLowerInvariant(), $rel
}
Set-Content -LiteralPath $shaPath -Encoding ASCII -Value $shaLines

Write-Output ("FORMULA_NEIGHBOR_MATRIX_ROWS {0}" -f $rows.Count)
Write-Output ("FORMULA_NEIGHBOR_GAP_ROWS {0}" -f $gapRows.Count)
Write-Output ("FORMULA_NEIGHBOR_FORMULA_CONTEXTS {0}" -f $formulaContextTotal)
Write-Output ("MANIFEST_ROWS {0}" -f $manifestRows.Count)
Write-Output ("SHA_LINES {0}" -f $shaLines.Count)
