$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper12_zh_translation_001_20260722'
$recordPath = Join-Path $workspace 'qa\HANS_MECHANICAL_BUILD_RECORD.json'
$logPath = Join-Path $workspace 'zh-Hans-CN\Noether_Paper12_Chinese_CurrentAuthority_zh-Hans-CN_v001.log'
$utf8 = [System.Text.UTF8Encoding]::new($false)
$originalRecordSha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $recordPath).Hash
$record = Get-Content -Raw -LiteralPath $recordPath | ConvertFrom-Json
$logText = [System.IO.File]::ReadAllText($logPath)
$pageMatches = [regex]::Matches($logText, '\((\d+) pages?')
if ($pageMatches.Count -lt 1) {
    throw 'Could not reparse a page count from the completed Hans engine log.'
}
$record.pdf.pages_reported_by_log = [int]$pageMatches[$pageMatches.Count - 1].Groups[1].Value
$record | Add-Member -NotePropertyName page_count_metadata_repair -NotePropertyValue ([ordered]@{
    repaired_local_time = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')
    original_record_sha256 = $originalRecordSha256
    reason = 'Initial wrapper regex required Output-written text and failed across MiKTeX log wrapping; final engine build had already completed successfully.'
    tex_or_pdf_changed = $false
    compilation_rerun = $false
    visual_inspection_performed = $false
})
[System.IO.File]::WriteAllText($recordPath, ($record | ConvertTo-Json -Depth 10), $utf8)
$record.page_count_metadata_repair | ConvertTo-Json -Depth 5

