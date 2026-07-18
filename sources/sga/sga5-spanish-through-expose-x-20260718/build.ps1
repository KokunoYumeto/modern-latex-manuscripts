param()

$ErrorActionPreference = 'Stop'
$Root = $PSScriptRoot
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Get-Artifact([string]$RelativePath) {
    $FullPath = Join-Path $Root $RelativePath
    if (-not (Test-Path -LiteralPath $FullPath)) {
        throw "Missing build artifact: $RelativePath"
    }
    $Item = Get-Item -LiteralPath $FullPath
    return [ordered]@{
        path = $RelativePath.Replace('\', '/')
        bytes = $Item.Length
        sha256 = (Get-FileHash -LiteralPath $FullPath -Algorithm SHA256).Hash
    }
}

Push-Location $Root
try {
    New-Item -ItemType Directory -Path 'output\pdf' -Force | Out-Null
    & powershell -NoProfile -ExecutionPolicy Bypass -File 'scripts\generate_evidence.ps1'
    if ($LASTEXITCODE -ne 0) {
        throw "Evidence generation failed with exit code $LASTEXITCODE"
    }

    & latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir='output\pdf' 'sga5_es.tex'
    if ($LASTEXITCODE -ne 0) {
        throw "latexmk failed with exit code $LASTEXITCODE"
    }

    $LogPath = Join-Path $Root 'output\pdf\sga5_es.log'
    $Log = [IO.File]::ReadAllText($LogPath)
    $ForbiddenDiagnostics = @(
        'LaTeX Warning:',
        'Package .* Warning:',
        'pdfTeX warning',
        'destination with the same identifier',
        'duplicate ignored',
        'Overfull \\[hv]box',
        'Underfull \\[hv]box',
        'Missing character:',
        'Undefined control sequence',
        'Fatal error'
    )
    $Failures = New-Object System.Collections.Generic.List[string]
    foreach ($Pattern in $ForbiddenDiagnostics) {
        $Matches = [regex]::Matches($Log, $Pattern, [Text.RegularExpressions.RegexOptions]::IgnoreCase)
        if ($Matches.Count -gt 0) {
            $Failures.Add("$Pattern=$($Matches.Count)")
        }
    }
    if ($Failures.Count -gt 0) {
        throw "Build log contains forbidden diagnostics: $($Failures -join '; ')"
    }

    $Target = Get-Content -LiteralPath 'evidence\TARGET_DOCUMENT_CURRENT.json' -Raw | ConvertFrom-Json
    $Build = [ordered]@{
        schema = 'sga5-build-evidence-v1'
        generated_utc = [DateTime]::UtcNow.ToString('o')
        status = 'pass'
        command = "latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=output\\pdf sga5_es.tex"
        target_document_sha256 = $Target.target_document_sha256
        source_document_sha256 = $Target.source_document_sha256
        forbidden_diagnostic_counts = [ordered]@{
            latex_warnings = 0
            package_warnings = 0
            pdftex_warnings = 0
            overfull_boxes = 0
            underfull_boxes = 0
            missing_characters = 0
            undefined_control_sequences = 0
            fatal_errors = 0
        }
        artifacts = @(
            (Get-Artifact 'build.ps1'),
            (Get-Artifact 'scripts\generate_evidence.ps1'),
            (Get-Artifact 'sga5_es.tex'),
            (Get-Artifact 'output\pdf\sga5_es.pdf'),
            (Get-Artifact 'output\pdf\sga5_es.log'),
            (Get-Artifact 'output\pdf\sga5_es.fls'),
            (Get-Artifact 'evidence\SOURCE_MANIFEST.csv'),
            (Get-Artifact 'evidence\SOURCE_ANOMALIES.md'),
            (Get-Artifact 'evidence\SPANISH_NATIVE_REGISTER_PROVENANCE.md'),
            (Get-Artifact 'evidence\UNIT_PARITY.csv'),
            (Get-Artifact 'evidence\UNIT_HASHES_CURRENT.csv'),
            (Get-Artifact 'evidence\TERMINOLOGY_DECISIONS.csv'),
            (Get-Artifact 'evidence\VISUAL_QA_WORKING.csv'),
            (Get-Artifact 'CONTINUATION_CURSOR.md'),
            (Get-Artifact 'STATUS.md'),
            (Get-Artifact 'evidence\TARGET_DOCUMENT_CURRENT.json')
        )
    }
    [IO.File]::WriteAllText((Join-Path $Root 'evidence\BUILD_CURRENT.json'), (($Build | ConvertTo-Json -Depth 8) + "`n"), $Utf8NoBom)
    $PdfArtifact = $Build.artifacts | Where-Object { $_.path -eq 'output/pdf/sga5_es.pdf' } | Select-Object -First 1
    Write-Output "Clean build: $($PdfArtifact.bytes) bytes; PDF SHA256 $($PdfArtifact.sha256); target SHA256 $($Target.target_document_sha256)"
}
finally {
    Pop-Location
}
