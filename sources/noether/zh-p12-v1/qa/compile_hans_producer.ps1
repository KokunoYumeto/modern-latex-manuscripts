$ErrorActionPreference = 'Stop'

$workspace = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper12_zh_translation_001_20260722'
$targetDir = Join-Path $workspace 'zh-Hans-CN'
$texName = 'Noether_Paper12_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex'
$texPath = Join-Path $targetDir $texName
$baseName = [System.IO.Path]::GetFileNameWithoutExtension($texName)
$utf8 = [System.Text.UTF8Encoding]::new($false)

if (-not (Test-Path -LiteralPath $texPath)) {
    throw "Missing Hans TeX: $texPath"
}

$passes = @()
for ($pass = 1; $pass -le 2; $pass++) {
    $passLog = Join-Path $targetDir ("{0}.pass{1}.stdout.txt" -f $baseName, $pass)
    Push-Location $targetDir
    try {
        & xelatex -interaction=nonstopmode -halt-on-error -file-line-error $texName 2>&1 |
            Tee-Object -FilePath $passLog
        $exitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
    }
    $passes += [ordered]@{pass = $pass; exit_code = $exitCode; stdout_path = [System.IO.Path]::GetFileName($passLog)}
    if ($exitCode -ne 0) {
        throw "XeLaTeX pass $pass failed with exit code $exitCode"
    }
}

$pdfPath = Join-Path $targetDir "$baseName.pdf"
$logPath = Join-Path $targetDir "$baseName.log"
if (-not (Test-Path -LiteralPath $pdfPath)) { throw "Expected PDF was not written: $pdfPath" }
if (-not (Test-Path -LiteralPath $logPath)) { throw "Expected log was not written: $logPath" }

function Get-Meta([string]$path) {
    $file = Get-Item -LiteralPath $path
    [ordered]@{
        path = $path.Substring($workspace.Length + 1).Replace('\', '/')
        bytes = $file.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
    }
}

$logText = [System.IO.File]::ReadAllText($logPath)
$pageMatch = [regex]::Match($logText, '\((\d+) pages?')
$record = [ordered]@{
    record_type = 'producer_mechanical_build'
    work_unit = 'Noether Paper 12'
    target_label = 'zh-Hans-CN'
    recorded_local_time = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')
    compiler = 'XeLaTeX'
    passes = $passes
    tex = Get-Meta $texPath
    pdf = (Get-Meta $pdfPath) + [ordered]@{
        pages_reported_by_log = if ($pageMatch.Success) { [int]$pageMatch.Groups[1].Value } else { $null }
        opened_or_rendered_by_producer = $false
    }
    log = (Get-Meta $logPath) + [ordered]@{
        error_pattern_matches = ([regex]::Matches($logText, '(?m)^!|Emergency stop|Fatal error')).Count
        warning_line_matches = ([regex]::Matches($logText, '(?m)^.*Warning.*$')).Count
        overfull_matches = ([regex]::Matches($logText, 'Overfull')).Count
        underfull_matches = ([regex]::Matches($logText, 'Underfull')).Count
    }
    epistemic_boundary = [ordered]@{
        compilation_success_is_translation_validation = $false
        source_check_performed = $false
        semantic_or_formula_check_performed = $false
        translation_quality_check_performed = $false
        visual_check_performed = $false
        independent_check = 'pending'
    }
}

[System.IO.File]::WriteAllText(
    (Join-Path $workspace 'qa\HANS_MECHANICAL_BUILD_RECORD.json'),
    ($record | ConvertTo-Json -Depth 8),
    $utf8
)
$record | ConvertTo-Json -Depth 8
