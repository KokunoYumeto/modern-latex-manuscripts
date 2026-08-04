$ErrorActionPreference = 'Stop'

$dir = $PSScriptRoot
$jsonl = Join-Path $dir 'DIFFICULTY_LEDGER.jsonl'
$csv = Join-Path $dir 'DIFFICULTY_LEDGER.csv'
if (Test-Path -LiteralPath $jsonl) { throw "Append-only ledger already exists; initializer refuses overwrite: $jsonl" }

$recordedAt = '2026-08-04T04:20:45.1622392+02:00'
$timePrecision = '100 ns-format clock string captured before append; actual system precision not independently established'
$sourceHash = '0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F'
$u01Hash = '48961F41A3C178968A5D2157F6FD5E756DAC7817555CAD07208C61E5A6643BE7'
$u02Hash = '52C02759CC6D08AA102DA366F7F148A4D148EC1066E2F81DE929CEE43A46DDDF'
$u03Hash = 'ECEE0AB9E9D8C89D6A9B4FBBA63128FBE1990764847E01038AB894EF66C9DF54'
$choicesHash = '7907AAB035347A041F0CE9288E00F980BA0A0132B3C733F54967FDFC7191254D'
$structuralReportHash = (Get-FileHash -LiteralPath (Join-Path $dir '..\structural_index\PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json') -Algorithm SHA256).Hash

function New-Issue {
    param(
        [string]$Id, [string[]]$Units, [string[]]$SourceLocators, [string[]]$TargetLocators,
        [string]$Symptom, [string[]]$Cause, [string[]]$Attempts, [string]$State,
        [string]$Resolution, [string[]]$Hashes, [string]$Residual,
        [string[]]$Cues, [string[]]$Decisions, [string[]]$Structures, [string]$Lesson
    )
    return [ordered]@{
        schema_version = '1.0'; issue_id = $Id; recorded_at = $recordedAt; time_precision = $timePrecision
        work_id = 'NOE-P01'; unit_ids = $Units; source_locators = $SourceLocators; target_locators = $TargetLocators
        symptom = $Symptom; cause_evidence = $Cause; attempts_and_rejections = $Attempts; state = $State
        resolution_or_hold = $Resolution; artifact_hashes = $Hashes
        tests_renders_reviews = [ordered]@{
            source_check = 'absent'; korean_review = 'absent'; formula_check = 'absent'; completeness_check = 'absent'
            compile = 'absent'; render = 'absent'; visual_review = 'absent'; human_or_external_review = 'absent'
            metadata_structural_validator = "pass; report SHA-256 $structuralReportHash; semantic scope excluded"
        }
        residual_risk = $Residual; recurrence_cues = $Cues; related_decision_ids = $Decisions
        related_structural_ids = $Structures; transferable_lesson = $Lesson
        claim_typing = [ordered]@{
            source_fact = 'exact stored German and target locators only'; computation = 'hashes and metadata validation only'
            editorial_inference = 'sense-window and risk classification'; model_preference = 'initial Korean producer wording'
            external_or_human_validation = 'absent'
        }
        previous_record_sha256 = $null
        record_sha256 = $null
    }
}

$issues = @(
    (New-Issue 'CJK-KO-P01-HARD-001' @('U01') @('German snapshot line 2') @('Korean U01 line 10') `
        'The literal cognate of biquadratisch can suggest a grouped biquadratic object rather than a homogeneous degree-four ternary form.' `
        @('The displayed special form has total variable degree four.','The source title says ternäre biquadratische Form.') `
        @('Selected 삼원 4차 형식 for mathematical transparency.','Rejected automatic 쌍이차 형식 as potentially misleading; retained it as a checker alternative.','Did not consult Chinese wording as Korean authority.') `
        'held' 'Producer choice frozen; independent Korean invariant-theory checker must adjudicate.' `
        @($sourceHash,$u01Hash,$choicesHash) 'A specialist may prefer an established Korean historical term even if it is less compositionally transparent.' `
        @('biquadratisch','quartic versus biquadratic','ternary-form titles') @('CJK-KO-P01-001','CJK-KO-P01-002') @('NOE-P01-KO-U01-TITLE-001') `
        'Translate the mathematical degree first, then expose literal historical alternatives as held rather than hiding the ambiguity.')

    (New-Issue 'CJK-KO-P01-HARD-002' @('U01') @('German snapshot line 13') @('Korean U01 line 22') `
        'Ordnung and Grad are false friends because the source assigns them different coefficient- and variable-degree senses in a footnote.' `
        @('The source footnote explicitly defines Ordnung by coefficients and Grad by variables.','The surrounding claims use both sixth Ordnung and sixth Grad.') `
        @('Selected 계수차수 and 변수차수.','Rejected one undifferentiated 차수 for both.','Rejected rank/order vocabulary that would obscure polynomial degree.') `
        'held' 'Local disambiguation retained; exact Korean historical terminology remains for checker review.' `
        @($sourceHash,$u01Hash,$choicesHash) 'The translation may over-regularize the source word Dimension and could diverge from specialist convention.' `
        @('Ordnung/Grad pair','coefficient degree','variable degree') @('CJK-KO-P01-002') @('NOE-P01-KO-U01-NOTE-002','NOE-P01-KO-U01-PARA-002') `
        'Whenever the source defines competing degree words, make the contrast explicit in the target and forbid fluent collapse to one attractor.')

    (New-Issue 'CJK-KO-P01-HARD-003' @('U01','U02') @('German snapshot lines 23-36') @('Korean U01 line 32','Korean U02 lines 9-20') `
        'Historical invariant-theory Modul collides with modern algebraic module, software module, and modular-arithmetic readings.' `
        @('The source treats a Modul as a stage-defining ground form and writes systems mod ν, mod s, and mod (ρ,t).','This sense differs from later Noether 가군 terminology.') `
        @('Retained 모듈 as a visibly provisional loan.','Rejected 가군 because it asserts the wrong algebraic object.','Rejected silently rewriting every occurrence as 법 because the source also treats the Modul as a Grundform.') `
        'held' 'Highest-priority terminology hold; checker must select a Korean historical invariant-theory rendering.' `
        @($sourceHash,$u01Hash,$u02Hash,$choicesHash) 'Readers can still import the modern module sense despite the producer note.' `
        @('Modul near mod notation','Grundform','module chains in invariant theory') @('CJK-KO-P01-002') @('NOE-P01-KO-U01-PARA-004','NOE-P01-KO-U02-PARA-001') `
        'A shared spelling across historical subfields is not a shared concept; preserve the source-local sense and route the headword for specialist review.')

    (New-Issue 'CJK-KO-P01-HARD-004' @('U01','U02','U03') @('German snapshot lines 23, 40-79') @('Korean U01 line 32','Korean U02 lines 24-42','Korean U03 lines 9-28') `
        'Überschiebung and Faltung are related invariant-theory operations but cannot be collapsed into one Korean label without losing the source distinction.' `
        @('Überschiebung appears in the general system-construction paragraph.','Faltung is separately defined by four factor-pair replacement operations and controls Formenreihe and Reduzent.') `
        @('Selected 전이연산 with German/English gloss for Überschiebung.','Selected 수축 for the explicitly defined Faltung.','Rejected one shared 수축 label for both.','Rejected literal 접기 because it foregrounds everyday folding rather than symbolic contraction.') `
        'held' 'Two-term distinction frozen as producer wording; exact Korean headwords await specialist adjudication.' `
        @($sourceHash,$u01Hash,$u02Hash,$u03Hash,$choicesHash) 'Established Korean invariant theory may name one or both operations differently, and transvection has geometric attractors.' `
        @('Überschiebung/transvection','Faltung/contraction','Grundfaltung','Formenreihe') @('CJK-KO-P01-002') @('NOE-P01-KO-U01-PARA-004','NOE-P01-KO-U02-DEFINITION-001','NOE-P01-KO-U02-THEOREM-001','NOE-P01-KO-U03-DEFINITION-001') `
        'Do not use lexical similarity or neighboring-language terminology to merge operations that the source defines separately.')

    (New-Issue 'CJK-KO-P01-HARD-005' @('U01','U02') @('German snapshot lines 2, 11, 13, 21, 36') @('Korean U01 lines 10, 19-32','Korean U02 line 20') `
        'Formensystem, Bildung, and the invariant/covariant/contravariant triad sit in a dense historical terminology cluster with several modern Korean attractors.' `
        @('Bildungen are counted members of a complete Formensystem.','The source distinguishes Invarianten, Kovarianten, and Kontravarianten by class.') `
        @('Selected 형식계 and 구성식.','Selected 불변식/공변식/반변식.','Rejected treating neighboring Chinese forms as Korean evidence.','Rejected unverified Hanja insertion.') `
        'held' 'Producer cluster retained with explicit sense windows; Korean disciplinary attestation remains absent.' `
        @($sourceHash,$u01Hash,$u02Hash,$choicesHash) 'Some terms may be readable but nonstandard, especially 구성식 and 반변식.' `
        @('Formensystem/Bildung','concomitant classes','형식 versus 형') @('CJK-KO-P01-002') @('NOE-P01-KO-U01-TITLE-001','NOE-P01-KO-U01-PARA-001','NOE-P01-KO-U01-PARA-002','NOE-P01-KO-U02-PARA-001') `
        'Treat a historical terminology cluster as a linked decision set; changing one headword may require re-evaluating its neighboring classes.')

    (New-Issue 'CJK-KO-P01-HARD-006' @('U03') @('German snapshot lines 66-79') @('Korean U03 lines 15-28') `
        'The reductant theorem nests causal and derivational clauses, and Reduzent is source-defined rather than a safely importable modern headword.' `
        @('The source defines Reduzent immediately before the theorem.','The theorem distinguishes Anfangsform, one Glied, Schlußform, and Gesamtformenreihe.') `
        @('Selected 환원자 and retained the definition in the target.','Kept the nested causal structure rather than replacing it with an unproved modern lemma form.','Rejected chemical-reductant interpretation and generic divisor language.') `
        'held' 'Clause structure and headword are frozen only as producer draft; mathematical fidelity check required.' `
        @($sourceHash,$u03Hash,$choicesHash) 'The Korean causal nesting may misidentify which member is contracted with the reductant; only an independent checker may resolve it.' `
        @('Reduzent','Anfangsform/Glied/Schlußform','double reduction') @('CJK-KO-P01-002') @('NOE-P01-KO-U03-DEFINITION-002','NOE-P01-KO-U03-THEOREM-001','NOE-P01-KO-U03-LIST-002') `
        'Source-defined theorem vocabulary should travel with its definition and exact locator; fluent paraphrase is not a substitute for a checker.')

    (New-Issue 'CJK-KO-P01-HARD-007' @('U01','U02','U03') @('Historical whole lines 381-460 / bytes [12505,20587)') @('SOURCE_CUSTODY.md; all Korean units') `
        'The historical whole-authority path disappeared after corpus consolidation, so the preserved interval is hash-stable but not yet rebound to one present current pointer.' `
        @('Preserved interval is 8,082 bytes with SHA-256 049998...8D2F.','Historical whole hash and pointer hash survive in custody records.','Sole canon task acknowledged the shared pointer debt but has not returned the Paper 1 binder.') `
        @('Translated from the immutable preserved interval with explicit lineage debt.','Rejected stale R821 as current.','Rejected local German comparison, adjudication, or patching.','Rejected giant archive inspection and broad filesystem search.') `
        'active_control' 'Hold current-canon wording claims until canon task 019fca5c-0e73-7c72-92fb-5b507b710598 returns the exact pointer/lineage receipt.' `
        @($sourceHash,'8AFE5BC676B48F76EE48F251F8E753B1ADCD6EA2500D1AD4927F4B531DD6F632') 'A later binder may show that this interval is a historical descendant rather than the present diplomatic head.' `
        @('missing old path','stale R821','preserved interval versus current pointer') @('CJK-KO-P01-001') @('NOE-P01-KO-WORK-001','NOE-P01-KO-U01','NOE-P01-KO-U02','NOE-P01-KO-U03') `
        'Hash-addressed interval custody can keep translation moving, but it must never be mislabeled as present canon while pointer lineage is unresolved.')

    (New-Issue 'CJK-KO-P01-HARD-008' @('U01','U02','U03') @('Checker-routing control; no German source defect') @('CHECKER_HANDOFF_U01_U03.md') `
        'No separately named independent Korean checker task exists in the bounded CJK controls or Chinese peer state.' `
        @('Chinese task 019f757c-95a5-7030-8b00-38762b5cdbfc explicitly returned that it has no Korean checker ID.','The Chinese lane performed no Korean review and refused to misuse the German canon task as a checker.') `
        @('Preserved an unchecked hash-pinned handoff.','Rejected asking Chinese or Japanese producers to authorize Korean.','Rejected creating a user-visible checker task without explicit routing authority.','Rejected treating task delivery as review.') `
        'active_control' 'Keep Paper 1 and Paper 42 UNCHECKED until PROJECT_COORDINATOR or an authorized lane route identifies an independent Korean checker.' `
        @($u01Hash,$u02Hash,$u03Hash,$choicesHash) 'Producer drafts may accumulate faster than checker capacity; terminology debt and formula risk remain open.' `
        @('missing checker ID','cross-language review temptation','delivery-versus-acceptance') @('CJK-KO-P42-004','CJK-KO-P01-002') @('NOE-P01-KO-WORK-001') `
        'An honest unavailable-checker state is better than inventing independence or laundering a peer translation task into review authority.')

    (New-Issue 'CJK-KO-P01-HARD-009' @('U01','U02','U03') @('difficulty-ledger initializer parser before any file write') @('evidence/difficulty_ledger/initialize_difficulty_ledger.ps1 line 45') `
        'The first initializer invocation failed with Missing closing parenthesis because multiline positional function arguments lacked explicit PowerShell continuation markers.' `
        @('Command exited 1 before DIFFICULTY_LEDGER.jsonl or CSV existed.','Parser identified line 45 at the first New-Issue call.','No translation or source file was touched by the failed invocation.') `
        @('Rejected hiding the failed initializer after repair.','Added explicit continuation markers to the same bounded calls.','Kept the initializer overwrite refusal so a rerun cannot silently replace an append-only ledger.') `
        'resolved' 'Initializer syntax repaired; failed approach retained in this record and validator evidence.' `
        @($sourceHash,$structuralReportHash) 'Future multiline PowerShell edits can recreate the same parse failure; the ledger initializer itself remains a one-time tool.' `
        @('multiline PowerShell positional calls','Missing closing parenthesis','initializer before durable write') @('CJK-KO-P01-003') @('NOE-P01-KO-WORK-001') `
        'Log pre-write tooling failures too: they explain why a durable artifact appeared only after a corrected invocation and prevent false claims of a clean first pass.')
)

$utf8 = [System.Text.UTF8Encoding]::new($false)
$sha = [System.Security.Cryptography.SHA256]::Create()
$previous = $null
$lines = [System.Collections.Generic.List[string]]::new()
$objects = [System.Collections.Generic.List[object]]::new()
try {
    foreach ($issue in $issues) {
        $issue.previous_record_sha256 = $previous
        $canonical = $issue | ConvertTo-Json -Compress -Depth 10
        $hash = ([System.BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes($canonical)))).Replace('-', '')
        $issue.record_sha256 = $hash
        $lines.Add(($issue | ConvertTo-Json -Compress -Depth 10))
        $objects.Add([pscustomobject]$issue)
        $previous = $hash
        $sha.Initialize()
    }
}
finally { $sha.Dispose() }
[System.IO.File]::WriteAllLines($jsonl, $lines, $utf8)

$objects | ForEach-Object {
    [pscustomobject]@{
        issue_id = $_.issue_id; recorded_at = $_.recorded_at; work_id = $_.work_id
        unit_ids_json = ($_.unit_ids | ConvertTo-Json -Compress); source_locators_json = ($_.source_locators | ConvertTo-Json -Compress)
        target_locators_json = ($_.target_locators | ConvertTo-Json -Compress); symptom = $_.symptom
        cause_evidence_json = ($_.cause_evidence | ConvertTo-Json -Compress); attempts_and_rejections_json = ($_.attempts_and_rejections | ConvertTo-Json -Compress)
        state = $_.state; resolution_or_hold = $_.resolution_or_hold; artifact_hashes_json = ($_.artifact_hashes | ConvertTo-Json -Compress)
        residual_risk = $_.residual_risk; recurrence_cues_json = ($_.recurrence_cues | ConvertTo-Json -Compress)
        related_decision_ids_json = ($_.related_decision_ids | ConvertTo-Json -Compress)
        related_structural_ids_json = ($_.related_structural_ids | ConvertTo-Json -Compress)
        transferable_lesson = $_.transferable_lesson; previous_record_sha256 = $_.previous_record_sha256; record_sha256 = $_.record_sha256
    }
} | Export-Csv -LiteralPath $csv -NoTypeInformation -Encoding utf8

Write-Output "initialized $($objects.Count) append-only records; chain head $previous"
