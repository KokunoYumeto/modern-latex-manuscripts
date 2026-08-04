param(
    [string]$Repository = 'C:\Users\Floris\Documents\interlanguage'
)

$ErrorActionPreference = 'Stop'
$work = Join-Path $Repository '03_projects\language_management\cjk\03_working_translations'
$out = Join-Path $work 'ko_noether'

function Get-DocumentBody([string]$path) {
    $raw = Get-Content -LiteralPath $path -Raw -Encoding utf8
    $match = [regex]::Match($raw, '(?s)\\begin\{document\}\s*(.*?)\s*\\end\{document\}')
    if (-not $match.Success) {
        throw "No document body in $path"
    }
    return $match.Groups[1].Value.Trim()
}

function Get-FragmentBody([string]$path) {
    $lines = Get-Content -LiteralPath $path -Encoding utf8
    $first = 0
    while ($first -lt $lines.Count -and ($lines[$first] -match '^\s*%' -or $lines[$first] -match '^\s*$')) {
        $first++
    }
    if ($first -ge $lines.Count) {
        throw "No translation body in $path"
    }
    return (($lines[$first..($lines.Count - 1)] -join "`n").Trim())
}

function Write-AssembledPaper([string]$paper, [string[]]$relativePaths) {
    $parts = foreach ($relative in $relativePaths) {
        $path = Join-Path $work $relative
        $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
        "% inherited: $relative`n% sha256: $hash`n$(Get-DocumentBody $path)"
    }
    $text = "% Korean Noether paper $paper — mechanically assembled inherited production body.`n" +
        "% Producer state only; independent checking and certification are outside this file.`n`n" +
        ($parts -join "`n`n") + "`n"
    [System.IO.File]::WriteAllText((Join-Path $out "p$paper.tex"), $text, [System.Text.UTF8Encoding]::new($false))
}

function Write-AssembledFragments([string]$paper, [string[]]$relativePaths) {
    $parts = foreach ($relative in $relativePaths) {
        $path = Join-Path $work $relative
        $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
        "% inherited: $relative`n% sha256: $hash`n$(Get-FragmentBody $path)"
    }
    $text = "% Korean Noether paper $paper — mechanically assembled inherited production body.`n" +
        "% Reopened against ED0004 by the current producer; independent checking remains external.`n`n" +
        ($parts -join "`n`n") + "`n"
    [System.IO.File]::WriteAllText((Join-Path $out "p$paper.tex"), $text, [System.Text.UTF8Encoding]::new($false))
}

Write-AssembledFragments '01' @(
    1..3 | ForEach-Object {
        'noether_paper01_ko_translation_001_20260804\ko\Noether_Paper01_Korean_U{0:D2}_translation_draft_v001.tex' -f $_
    }
)
Write-AssembledFragments '03' @(
    1..3 | ForEach-Object {
        'noether_paper03_ko_translation_001_20260804\targets\Noether_P03_Korean_U{0:D2}_UNCHECKED.tex' -f $_
    }
)
Write-AssembledFragments '05' @(
    1..4 | ForEach-Object {
        'noether_paper05_ko_translation_001_20260804\targets\Noether_P05_Korean_U{0:D2}_UNCHECKED.tex' -f $_
    }
)
Write-AssembledFragments '07' @(
    1..8 | ForEach-Object {
        'noether_paper07_ko_translation_001_20260804\targets\Noether_P07_Korean_U{0:D2}_UNCHECKED.tex' -f $_
    }
)
Write-AssembledFragments '08' @(
    1..36 | ForEach-Object {
        $unit = $_
        $tranche = switch ($unit) {
            { $_ -le 3 } { 1; break }
            { $_ -le 7 } { 2; break }
            { $_ -le 13 } { 3; break }
            { $_ -le 17 } { 4; break }
            { $_ -le 21 } { 5; break }
            { $_ -le 26 } { 6; break }
            { $_ -le 31 } { 7; break }
            default { 8 }
        }
        'noether_paper08_ko_translation_001_20260804\targets\T{0:D2}_U{1:D2}.tex' -f $tranche, $unit
    }
)
Write-AssembledFragments '41' @(
    1..12 | ForEach-Object {
        'noether_paper41_ko_translation_001_20260804\targets\Noether_P41_Korean_U{0:D2}_UNCHECKED.tex' -f $_
    }
)
Write-AssembledFragments '42' @(
    1..12 | ForEach-Object {
        'noether_paper42_ko_translation_001_20260804\ko\Noether_Paper42_Korean_U{0:D2}_translation_draft_v001.tex' -f $_
    }
)

$p05 = Join-Path $out 'p05.tex'
$p05Text = Get-Content -LiteralPath $p05 -Raw -Encoding utf8
$p05Text = $p05Text.Replace('정칙 유리결합, 곧 다항식적 결합', '다항식적 결합')
$p05Text = $p05Text.Replace('상대 정칙 함수의 문제', '상대적으로 정수적인 함수의 문제')
$p05Text = $p05Text.Replace('모든 정칙 유리 사영불변식은 판별식의 정칙 함수', '모든 다항 사영불변식은 판별식의 다항함수')
[System.IO.File]::WriteAllText($p05, $p05Text, [System.Text.UTF8Encoding]::new($false))

$p41 = Join-Path $out 'p41.tex'
$p41Text = Get-Content -LiteralPath $p41 -Raw -Encoding utf8
$p41Text = $p41Text.Replace('\(A\)를 \(K\)에 대한 계수 \(n\)의 선형형식 가군으로 둔다', '\(A\)를 \(K\) 위에서 랭크 \(n\)인 선형형식 모듈로 둔다')
$p41Text = $p41Text.Replace('따라서 \(k\) 위에서 계수 \(n^2\)인 대수', '따라서 \(k\) 위에서 차원 \(n^2\)인 대수')
$p41Text = $p41Text.Replace('모든 (정칙) 원소', '모든 (가역) 원소')
$p41Text = $p41Text.Replace('슈어 지표', '슈어 지수')
$p41Text = $p41Text.Replace('\text{also}', '\text{따라서}')
[System.IO.File]::WriteAllText($p41, $p41Text, [System.Text.UTF8Encoding]::new($false))

$p42 = Join-Path $out 'p42.tex'
$p42Text = Get-Content -LiteralPath $p42 -Raw -Encoding utf8
$p42Text = $p42Text.Replace('그 계수는 $K$의 계수와 일치한다. 왜냐하면 $\bar K E_\Hh$의 $\bar k$ 위 계수는 $n$이고', '그 랭크는 $K$의 랭크와 일치한다. 왜냐하면 $\bar K E_\Hh$의 $\bar k$ 위 랭크는 $n$이고')
$p42Text = $p42Text.Replace('$\bar K$의 $\bar k$ 위 계수는 $nh$', '$\bar K$의 $\bar k$ 위 랭크는 $nh$')
$p42Text = $p42Text.Replace('전계수', '최대 랭크')
$p42Text = $p42Text.Replace('$\mathfrak L$이 정칙인 경우에는 $a$의 계수가 $n$', '$\mathfrak L$이 정칙(최대 랭크)인 경우에는 $a$의 랭크가 $n$')
$p42Text = $p42Text.Replace('가군 $\mathfrak C$의 계수에 관하여 아무 가정도 하지 않는다는', '가군 $\mathfrak C$의 랭크에 관하여 아무 가정도 하지 않는다는')
[System.IO.File]::WriteAllText($p42, $p42Text, [System.Text.UTF8Encoding]::new($false))

Write-AssembledPaper '26' @(
    'noether_paper26_cjk_tranche_002_20260717\ko\Noether_Paper26_Korean_v001.tex'
)
Write-AssembledPaper '27' @(
    'noether_paper27_ko_tranche_001_20260718\ko\Noether_Paper27_Korean_v001.tex'
)
Write-AssembledPaper '28' @(
    'noether_paper28_cjk_tranche_003_20260718\ko\Noether_Paper28_Korean_v001.tex'
)
$p28 = Join-Path $out 'p28.tex'
$p28Text = Get-Content -LiteralPath $p28 -Raw -Encoding utf8
$p28Text = $p28Text.Replace('완전가약환(오늘날의 반단순환)', '완전가약환')
[System.IO.File]::WriteAllText($p28, $p28Text, [System.Text.UTF8Encoding]::new($false))
Write-AssembledPaper '29' @(
    'noether_paper29_ko_tranche_001_20260718\ko\Noether_Paper29_Korean_U01_v001.tex',
    'noether_paper29_ko_tranche_001_20260718\ko\Noether_Paper29_Korean_U02_v001.tex',
    'noether_paper29_ko_tranche_001_20260718\ko\Noether_Paper29_Korean_U03_v001.tex',
    'noether_paper29_ko_tranche_001_20260718\ko\Noether_Paper29_Korean_U04_v001.tex',
    'noether_paper29_ko_tranche_001_20260718\ko\Noether_Paper29_Korean_U05_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U06_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U07_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U08_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U09_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U10_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U11_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U12_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U13_translation_draft_v001.tex',
    'noether_paper29_ko_tranche_002_20260722\ko\Noether_Paper29_Korean_U14_translation_draft_v001.tex'
)
Write-AssembledPaper '32' @(
    1..19 | ForEach-Object {
        'noether_paper32_ko_translation_001_20260722\ko\Noether_Paper32_Korean_U{0:D2}_translation_draft_v001.tex' -f $_
    }
)
Write-AssembledPaper '33' @(
    1..8 | ForEach-Object {
        'noether_paper33_ko_translation_001_20260722\ko\Noether_Paper33_Korean_U{0:D2}_translation_draft_v001.tex' -f $_
    }
)
Write-AssembledPaper '36' @(
    'noether_paper36_cjk_tranche_001_20260717\ko\Noether_Paper36_Korean_v001.tex'
)

$p29 = Join-Path $out 'p29.tex'
$p29Text = Get-Content -LiteralPath $p29 -Raw -Encoding utf8
$p29Text = $p29Text.Replace('\mathfrak K$는 $\mathfrak R$의 분수체\footnote{원논문 28쪽 각주 2 참조.}', '\mathfrak K$는 $\mathfrak R$의 분수체\footnotemark[\value{footnote}]')
[System.IO.File]::WriteAllText($p29, $p29Text, [System.Text.UTF8Encoding]::new($false))

$p32 = Join-Path $out 'p32.tex'
$p32Text = Get-Content -LiteralPath $p32 -Raw -Encoding utf8
$p32Text = $p32Text.Replace('최소 차수의 모든 분해체는 이들 가운데 하나이다.', '최소 차수의 모든 분해체는 그들 가운데 하나에 포함된다.')
[System.IO.File]::WriteAllText($p32, $p32Text, [System.Text.UTF8Encoding]::new($false))
