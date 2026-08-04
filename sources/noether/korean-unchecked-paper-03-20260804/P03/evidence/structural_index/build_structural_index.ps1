[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$indexDir = $PSScriptRoot
$root = (Resolve-Path -LiteralPath (Join-Path $indexDir '..\..')).Path
$sourcePath = '${PUBLIC_INTERLANGUAGE_ROOT}\03_projects\noether\07_german_canon_control\candidates\NOETH-DE-ED-0001\Noether_German_NOETH-DE-ED-0001.tex'
$sourceHashExpected = 'D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB'
$paperIntervalHashExpected = 'E600FD2A19ACA22F43D54FB65C61B79172B12FE5AB09446A2C9C9B8CACD26E7D'
$pointerId = 'NOETH-DE-AUTH-v003-20260804'
$pointerHash = '932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$targets = [ordered]@{
    U01 = Join-Path $root 'targets\Noether_P03_Korean_U01_UNCHECKED.tex'
    U02 = Join-Path $root 'targets\Noether_P03_Korean_U02_UNCHECKED.tex'
    U03 = Join-Path $root 'targets\Noether_P03_Korean_U03_UNCHECKED.tex'
}
$targetHashExpected = [ordered]@{
    U01 = '057D6EAECAAB02C4D19C6908276C11E32953748726BD36B628712AB5C5E78ECB'
    U02 = 'A2A9F68B55C15EEFEAE178B4F24CB5D56222E563F6B5A126F46D1AA75BEA38B1'
    U03 = '7942126177C707C89F67444BE020F90F2139C0C5036A153297C0A7F83119F4B4'
}
$unitSource = [ordered]@{
    U01 = [ordered]@{ start = 3573; end = 3584; bytes = 2156; sha256 = 'DF50EAD7065F663901F51ADFCA37A138921063362CA449665D37B855921B496C' }
    U02 = [ordered]@{ start = 3586; end = 3594; bytes = 2975; sha256 = 'A7B7CA981F7B8D6B32171BF0709E27440A25B2754642BD095304E54A5A25D5C6' }
    U03 = [ordered]@{ start = 3596; end = 3608; bytes = 3144; sha256 = '0D110465AEE20E18EE1427577D33D435FCF97D5CA99BEF3878EF52DC341F01A5' }
}
$unitTargetBody = [ordered]@{
    U01 = @(14, 25)
    U02 = @(12, 20)
    U03 = @(14, 26)
}
$unitCursor = [ordered]@{
    U01 = 'continue at whole-authority line 3586 / Korean U02'
    U02 = 'continue at whole-authority line 3596 / Korean U03'
    U03 = 'Paper 3 interval exhausted after whole-authority line 3608; lines 3609--3610 excluded; await independent Korean checker'
    ALL = 'Paper 3 interval exhausted after whole-authority line 3608; lines 3609--3610 excluded; await independent Korean checker'
}

function Get-FileSha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Get-Utf8Sha256([AllowNull()][object]$Text) {
    if ($null -eq $Text) { return $null }
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([System.BitConverter]::ToString($sha.ComputeHash($utf8NoBom.GetBytes($Text)))).Replace('-', '')
    }
    finally { $sha.Dispose() }
}

$lineCache = @{}
function Get-PathLines([string]$Path) {
    if (-not $lineCache.ContainsKey($Path)) {
        $lineCache[$Path] = [System.IO.File]::ReadAllLines($Path, $utf8NoBom)
    }
    return $lineCache[$Path]
}

function Get-LfSliceInfo([string]$Path, [int]$Start, [int]$End) {
    $lines = @(Get-PathLines $Path)
    if ($Start -lt 1 -or $End -lt $Start -or $End -gt $lines.Count) {
        throw "Invalid line slice $Start-$End for $Path with $($lines.Count) lines"
    }
    $text = [string]::Join("`n", $lines[($Start - 1)..($End - 1)]) + "`n"
    $bytes = $utf8NoBom.GetBytes($text)
    return [ordered]@{ sha256 = Get-Utf8Sha256 $text; bytes = $bytes.Length }
}

function Get-InlineMathFragments([string]$Text) {
    $items = [System.Collections.Generic.List[string]]::new()
    $pattern = '\$[^$\r\n]*\$|\\\((?:(?!\\\)).)*\\\)'
    foreach ($match in [System.Text.RegularExpressions.Regex]::Matches($Text, $pattern)) {
        [void]$items.Add($match.Value)
    }
    return $items.ToArray()
}

function New-Spec {
    param(
        [Parameter(Mandatory)][string]$Id,
        [Parameter(Mandatory)][string]$Type,
        [Parameter(Mandatory)][string]$Label,
        [AllowNull()][object]$Parent,
        [Parameter(Mandatory)][int]$Order,
        [Parameter(Mandatory)][ValidateSet('ALL','U01','U02','U03')][string]$Unit,
        [Parameter(Mandatory)][int]$SourceStart,
        [Parameter(Mandatory)][int]$SourceEnd,
        [Parameter(Mandatory)][int]$TargetStart,
        [Parameter(Mandatory)][int]$TargetEnd,
        [string[]]$Basis = @('producer_editorial_inference'),
        [string[]]$Relations = @(),
        [AllowNull()][object]$SourceFragment = $null,
        [AllowNull()][object]$SourceOccurrence = $null,
        [AllowNull()][object]$TargetFragment = $null,
        [AllowNull()][object]$TargetOccurrence = $null
    )
    return [pscustomobject]@{
        id = $Id
        type = $Type
        label = $Label
        parent = $Parent
        order = $Order
        unit = $Unit
        source_start = $SourceStart
        source_end = $SourceEnd
        target_start = $TargetStart
        target_end = $TargetEnd
        basis = @($Basis)
        relations = @($Relations)
        source_fragment = $SourceFragment
        source_occurrence = $SourceOccurrence
        target_fragment = $TargetFragment
        target_occurrence = $TargetOccurrence
    }
}

$specs = [System.Collections.Generic.List[object]]::new()
function Add-Spec([object]$Spec) { [void]$specs.Add($Spec) }

$formulaCounter = @{ U01 = 0; U02 = 0; U03 = 0 }
function Add-InlineMathGroup {
    param(
        [string]$GroupId, [string]$Parent, [int]$Order, [ValidateSet('U01','U02','U03')][string]$Unit,
        [int]$SourceLine, [int]$TargetLine, [string]$Label
    )
    Add-Spec (New-Spec -Id $GroupId -Type 'other' -Label $Label -Parent $Parent -Order $Order -Unit $Unit `
        -SourceStart $SourceLine -SourceEnd $SourceLine -TargetStart $TargetLine -TargetEnd $TargetLine `
        -Basis @('source_fact','computation','producer_editorial_inference'))

    $sourceText = (Get-PathLines $sourcePath)[$SourceLine - 1]
    $targetText = (Get-PathLines $targets[$Unit])[$TargetLine - 1]
    $sourceFragments = @(Get-InlineMathFragments $sourceText)
    $targetFragments = @(Get-InlineMathFragments $targetText)
    $count = [Math]::Max($sourceFragments.Count, $targetFragments.Count)
    for ($i = 0; $i -lt $count; $i++) {
        $formulaCounter[$Unit]++
        $id = 'NOE-P03-KO-{0}-FORMULA-{1:D3}' -f $Unit, $formulaCounter[$Unit]
        $sourceFragment = if ($i -lt $sourceFragments.Count) { [string]$sourceFragments[$i] } else { $null }
        $targetFragment = if ($i -lt $targetFragments.Count) { [string]$targetFragments[$i] } else { $null }
        $sourceOccurrence = if ($null -ne $sourceFragment) { $i + 1 } else { $null }
        $targetOccurrence = if ($null -ne $targetFragment) { $i + 1 } else { $null }
        Add-Spec (New-Spec -Id $id -Type 'formula' `
            -Label "Inline math occurrence $($i + 1) on source line $SourceLine / target line $TargetLine" `
            -Parent $GroupId -Order ($i + 1) -Unit $Unit `
            -SourceStart $SourceLine -SourceEnd $SourceLine -TargetStart $TargetLine -TargetEnd $TargetLine `
            -Basis @('source_fact','computation','producer_editorial_inference') `
            -Relations @("formula_in|$GroupId") `
            -SourceFragment $sourceFragment -SourceOccurrence $sourceOccurrence `
            -TargetFragment $targetFragment -TargetOccurrence $targetOccurrence)
    }
}

function Add-LineFormula {
    param(
        [string]$Parent, [int]$Order, [ValidateSet('U01','U02','U03')][string]$Unit,
        [int]$SourceLine, [int]$TargetLine, [string]$Label
    )
    $formulaCounter[$Unit]++
    $id = 'NOE-P03-KO-{0}-FORMULA-{1:D3}' -f $Unit, $formulaCounter[$Unit]
    Add-Spec (New-Spec -Id $id -Type 'formula' -Label $Label -Parent $Parent -Order $Order -Unit $Unit `
        -SourceStart $SourceLine -SourceEnd $SourceLine -TargetStart $TargetLine -TargetEnd $TargetLine `
        -Basis @('source_fact','computation','producer_editorial_inference') -Relations @("formula_in|$Parent"))
}

# Work and unit containers.
Add-Spec (New-Spec -Id 'NOE-P03-KO-WORK-001' -Type 'work' -Label 'Paper 3 complete bounded translation interval' -Parent $null -Order 1 -Unit 'ALL' `
    -SourceStart 3573 -SourceEnd 3608 -TargetStart 1 -TargetEnd 1 -Basis @('source_fact','computation') `
    -Relations @('contains|NOE-P03-KO-U01-UNIT-001','contains|NOE-P03-KO-U02-UNIT-001','contains|NOE-P03-KO-U03-UNIT-001'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-UNIT-001' -Type 'unit' -Label 'Title, motivation, ternary symbolic method, and contraction result' -Parent 'NOE-P03-KO-WORK-001' -Order 1 -Unit 'U01' `
    -SourceStart 3573 -SourceEnd 3584 -TargetStart 14 -TargetEnd 25 -Basis @('source_fact','computation'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-UNIT-001' -Type 'unit' -Label 'n-ary coordinate rows, corresponding matrices, and display (1)' -Parent 'NOE-P03-KO-WORK-001' -Order 2 -Unit 'U02' `
    -SourceStart 3586 -SourceEnd 3594 -TargetStart 12 -TargetEnd 20 -Basis @('source_fact','computation') `
    -Relations @('continues|NOE-P03-KO-U01-UNIT-001'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-UNIT-001' -Type 'unit' -Label 'Converse representation, decomposition identity, and final contraction theorem' -Parent 'NOE-P03-KO-WORK-001' -Order 3 -Unit 'U03' `
    -SourceStart 3596 -SourceEnd 3608 -TargetStart 14 -TargetEnd 26 -Basis @('source_fact','computation') `
    -Relations @('continues|NOE-P03-KO-U02-UNIT-001'))

# U01 explicit title block and prose structure.
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-OTHER-001' -Type 'other' -Label 'Centered title, byline, and publication block' -Parent 'NOE-P03-KO-U01-UNIT-001' -Order 1 -Unit 'U01' `
    -SourceStart 3573 -SourceEnd 3579 -TargetStart 14 -TargetEnd 20 -Basis @('source_fact','computation'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-TITLE-001' -Type 'title' -Label 'Zur Invariantentheorie der Formen von n Variabeln' -Parent 'NOE-P03-KO-U01-OTHER-001' -Order 1 -Unit 'U01' `
    -SourceStart 3574 -SourceEnd 3574 -TargetStart 15 -TargetEnd 15 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-FOOTNOTE-001' -Type 'footnote' -Label '1909 Salzburg lecture provenance' -Parent 'NOE-P03-KO-TITLE-001' -Order 1 -Unit 'U01' `
    -SourceStart 3574 -SourceEnd 3574 -TargetStart 15 -TargetEnd 15 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('note_for|NOE-P03-KO-TITLE-001'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U01-OTHER-002' -Parent 'NOE-P03-KO-TITLE-001' -Order 2 -Unit 'U01' -SourceLine 3574 -TargetLine 15 -Label 'Title inline-math occurrence group'
Add-Spec (New-Spec -Id 'NOE-P03-KO-AUTHOR-001' -Type 'author' -Label 'Emmy Noether byline in Erlangen' -Parent 'NOE-P03-KO-U01-OTHER-001' -Order 2 -Unit 'U01' `
    -SourceStart 3576 -SourceEnd 3576 -TargetStart 17 -TargetEnd 17 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-PUBLICATION-NOTE-001' -Type 'publication_note' -Label 'Jahresbericht der DMV 19 (1910), pages 101--104' -Parent 'NOE-P03-KO-U01-OTHER-001' -Order 3 -Unit 'U01' `
    -SourceStart 3578 -SourceEnd 3578 -TargetStart 19 -TargetEnd 19 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-BIBLIOGRAPHY-ITEM-001' -Type 'bibliography_item' -Label 'Paper publication citation in Jahresbericht der DMV' -Parent 'NOE-P03-KO-PUBLICATION-NOTE-001' -Order 1 -Unit 'U01' `
    -SourceStart 3578 -SourceEnd 3578 -TargetStart 19 -TargetEnd 19 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('bibliography_for|NOE-P03-KO-PUBLICATION-NOTE-001'))

Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-PARAGRAPH-001' -Type 'paragraph' -Label 'Projective invariant-theory status, open methods, and announced scope' -Parent 'NOE-P03-KO-U01-UNIT-001' -Order 2 -Unit 'U01' `
    -SourceStart 3582 -SourceEnd 3582 -TargetStart 23 -TargetEnd 23 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-001' -Type 'closed_prose' -Label 'Main problem and finiteness statement' -Parent 'NOE-P03-KO-U01-PARAGRAPH-001' -Order 1 -Unit 'U01' `
    -SourceStart 3582 -SourceEnd 3582 -TargetStart 23 -TargetEnd 23 -Basis @('producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-002' -Type 'closed_prose' -Label 'Untreated questions about methods for form relations' -Parent 'NOE-P03-KO-U01-PARAGRAPH-001' -Order 2 -Unit 'U01' `
    -SourceStart 3582 -SourceEnd 3582 -TargetStart 23 -TargetEnd 23 -Basis @('producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-003' -Type 'closed_prose' -Label 'Announcement and ternary-domain sketch' -Parent 'NOE-P03-KO-U01-PARAGRAPH-001' -Order 3 -Unit 'U01' `
    -SourceStart 3582 -SourceEnd 3582 -TargetStart 23 -TargetEnd 23 -Basis @('producer_editorial_inference'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U01-OTHER-003' -Parent 'NOE-P03-KO-U01-PARAGRAPH-001' -Order 4 -Unit 'U01' -SourceLine 3582 -TargetLine 23 -Label 'First prose paragraph inline-math occurrence group'

Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-PARAGRAPH-002' -Type 'paragraph' -Label 'Fundamental symbolic theorems, generating processes, and contractions' -Parent 'NOE-P03-KO-U01-UNIT-001' -Order 3 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-004' -Type 'closed_prose' -Label 'Two fundamental theorems of the symbolic method' -Parent 'NOE-P03-KO-U01-PARAGRAPH-002' -Order 1 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-THEOREM-001' -Type 'theorem' -Label 'All invariant formations admit symbolic representation' -Parent 'NOE-P03-KO-U01-CLOSED-PROSE-004' -Order 1 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U01-PARAGRAPH-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-THEOREM-002' -Type 'theorem' -Label 'Invariant relations arise through finitely many symbolic identities' -Parent 'NOE-P03-KO-U01-CLOSED-PROSE-004' -Order 2 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U01-PARAGRAPH-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-FOOTNOTE-002' -Type 'footnote' -Label 'Study reference for ternary-form methods' -Parent 'NOE-P03-KO-U01-CLOSED-PROSE-004' -Order 3 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('note_for|NOE-P03-KO-U01-THEOREM-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-BIBLIOGRAPHY-ITEM-002' -Type 'bibliography_item' -Label 'Study, Methoden zur Theorie der ternären Formen, II section 6' -Parent 'NOE-P03-KO-U01-FOOTNOTE-002' -Order 1 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('bibliography_for|NOE-P03-KO-U01-FOOTNOTE-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-005' -Type 'closed_prose' -Label 'Processes for generating forms and series developments' -Parent 'NOE-P03-KO-U01-PARAGRAPH-002' -Order 2 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-006' -Type 'closed_prose' -Label 'Dissertation theorem on generation of contractions' -Parent 'NOE-P03-KO-U01-PARAGRAPH-002' -Order 3 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-THEOREM-003' -Type 'theorem' -Label 'All contractions generated by two cogredient contractions in the ternary case' -Parent 'NOE-P03-KO-U01-CLOSED-PROSE-006' -Order 1 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U01-PARAGRAPH-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-FOOTNOTE-003' -Type 'footnote' -Label 'Dissertation reference for the ternary biquadratic form system' -Parent 'NOE-P03-KO-U01-CLOSED-PROSE-006' -Order 2 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('note_for|NOE-P03-KO-U01-THEOREM-003'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-BIBLIOGRAPHY-ITEM-003' -Type 'bibliography_item' -Label 'Noether dissertation reference in Crelle journal volume 134' -Parent 'NOE-P03-KO-U01-FOOTNOTE-003' -Order 1 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('bibliography_for|NOE-P03-KO-U01-FOOTNOTE-003'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-007' -Type 'closed_prose' -Label 'Identification of the two contractions in a symbolic product' -Parent 'NOE-P03-KO-U01-PARAGRAPH-002' -Order 4 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('producer_editorial_inference'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U01-OTHER-004' -Parent 'NOE-P03-KO-U01-CLOSED-PROSE-007' -Order 1 -Unit 'U01' -SourceLine 3584 -TargetLine 25 -Label 'Contraction example inline-math occurrence group'
Add-Spec (New-Spec -Id 'NOE-P03-KO-U01-CLOSED-PROSE-008' -Type 'closed_prose' -Label 'Reduction-theory consequence' -Parent 'NOE-P03-KO-U01-PARAGRAPH-002' -Order 5 -Unit 'U01' `
    -SourceStart 3584 -SourceEnd 3584 -TargetStart 25 -TargetEnd 25 -Basis @('producer_editorial_inference'))

# U02 paragraphs, theorems, note, and display (1).
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-PARAGRAPH-001' -Type 'paragraph' -Label 'Limits of determinant symbolism in the n-ary domain' -Parent 'NOE-P03-KO-U02-UNIT-001' -Order 1 -Unit 'U02' `
    -SourceStart 3586 -SourceEnd 3586 -TargetStart 12 -TargetEnd 12 -Basis @('source_fact','producer_editorial_inference'))
$u02p1Labels = @(
    'Conditional scope of the first symbolic theorem beyond the ternary case',
    'Point, plane, and line coordinates in the quaternary case',
    'n-ary variable rows and symbol rows',
    'Condition for determinant-based symbolic representation',
    'Determinant aggregates depending on symbol rows',
    'Loss of the remaining ternary-domain theorems'
)
for ($i = 0; $i -lt $u02p1Labels.Count; $i++) {
    Add-Spec (New-Spec -Id ('NOE-P03-KO-U02-CLOSED-PROSE-{0:D3}' -f ($i + 1)) -Type 'closed_prose' -Label $u02p1Labels[$i] `
        -Parent 'NOE-P03-KO-U02-PARAGRAPH-001' -Order ($i + 1) -Unit 'U02' -SourceStart 3586 -SourceEnd 3586 -TargetStart 12 -TargetEnd 12 `
        -Basis @('producer_editorial_inference'))
}
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U02-OTHER-001' -Parent 'NOE-P03-KO-U02-PARAGRAPH-001' -Order 7 -Unit 'U02' -SourceLine 3586 -TargetLine 12 -Label 'Coordinate and symbol-row inline-math occurrence group'

Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-PARAGRAPH-002' -Type 'paragraph' -Label 'Corresponding matrices and explicit symbol-row representation' -Parent 'NOE-P03-KO-U02-UNIT-001' -Order 2 -Unit 'U02' `
    -SourceStart 3588 -SourceEnd 3588 -TargetStart 14 -TargetEnd 14 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-CLOSED-PROSE-007' -Type 'closed_prose' -Label 'Principle for explicit representation in symbol rows' -Parent 'NOE-P03-KO-U02-PARAGRAPH-002' -Order 1 -Unit 'U02' `
    -SourceStart 3588 -SourceEnd 3588 -TargetStart 14 -TargetEnd 14 -Basis @('producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-CLOSED-PROSE-008' -Type 'closed_prose' -Label 'Corresponding-matrices theorem statement' -Parent 'NOE-P03-KO-U02-PARAGRAPH-002' -Order 2 -Unit 'U02' `
    -SourceStart 3588 -SourceEnd 3588 -TargetStart 14 -TargetEnd 14 -Basis @('producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-THEOREM-001' -Type 'theorem' -Label 'One-to-one correspondence between p-rho and q-(n-rho) rows' -Parent 'NOE-P03-KO-U02-CLOSED-PROSE-008' -Order 1 -Unit 'U02' `
    -SourceStart 3588 -SourceEnd 3588 -TargetStart 14 -TargetEnd 14 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U02-PARAGRAPH-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-CLOSED-PROSE-009' -Type 'closed_prose' -Label 'Corresponding symbol-row construction' -Parent 'NOE-P03-KO-U02-PARAGRAPH-002' -Order 3 -Unit 'U02' `
    -SourceStart 3588 -SourceEnd 3588 -TargetStart 14 -TargetEnd 14 -Basis @('producer_editorial_inference'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U02-OTHER-002' -Parent 'NOE-P03-KO-U02-PARAGRAPH-002' -Order 4 -Unit 'U02' -SourceLine 3588 -TargetLine 14 -Label 'Corresponding-matrices inline-math occurrence group'

Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-PARAGRAPH-003' -Type 'paragraph' -Label 'Second formulation and lead-in to display (1)' -Parent 'NOE-P03-KO-U02-UNIT-001' -Order 3 -Unit 'U02' `
    -SourceStart 3590 -SourceEnd 3590 -TargetStart 16 -TargetEnd 16 -Basis @('source_fact','producer_editorial_inference'))
$u02p3Labels = @(
    'Matrix product assigned to a determinant',
    'Converse conversion of a determinant to a matrix product',
    'Equivalence and reformulation of the first symbolic theorem',
    'Construction from two symbol rows and variable rows',
    'Lead-in to the displayed matrix product'
)
for ($i = 0; $i -lt $u02p3Labels.Count; $i++) {
    Add-Spec (New-Spec -Id ('NOE-P03-KO-U02-CLOSED-PROSE-{0:D3}' -f ($i + 10)) -Type 'closed_prose' -Label $u02p3Labels[$i] `
        -Parent 'NOE-P03-KO-U02-PARAGRAPH-003' -Order ($i + 1) -Unit 'U02' -SourceStart 3590 -SourceEnd 3590 -TargetStart 16 -TargetEnd 16 `
        -Basis @('producer_editorial_inference'))
}
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-THEOREM-002' -Type 'theorem' -Label 'Matrix-product formulation and converse determinant conversion' -Parent 'NOE-P03-KO-U02-CLOSED-PROSE-010' -Order 1 -Unit 'U02' `
    -SourceStart 3590 -SourceEnd 3590 -TargetStart 16 -TargetEnd 16 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U02-PARAGRAPH-003','cross_reference|NOE-P03-KO-U02-CLOSED-PROSE-011'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-FOOTNOTE-001' -Type 'footnote' -Label 'Explanation of matrix product as a sum of products of corresponding determinants' -Parent 'NOE-P03-KO-U02-THEOREM-002' -Order 1 -Unit 'U02' `
    -SourceStart 3590 -SourceEnd 3590 -TargetStart 16 -TargetEnd 16 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('note_for|NOE-P03-KO-U02-THEOREM-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-THEOREM-003' -Type 'theorem' -Label 'All invariant formations admit symbolic representation by matrix products' -Parent 'NOE-P03-KO-U02-CLOSED-PROSE-012' -Order 1 -Unit 'U02' `
    -SourceStart 3590 -SourceEnd 3590 -TargetStart 16 -TargetEnd 16 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U02-PARAGRAPH-003'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U02-OTHER-003' -Parent 'NOE-P03-KO-U02-PARAGRAPH-003' -Order 6 -Unit 'U02' -SourceLine 3590 -TargetLine 16 -Label 'Matrix-product paragraph inline-math occurrence group'
Add-Spec (New-Spec -Id 'NOE-P03-KO-U02-DISPLAY-001' -Type 'display' -Label 'Numbered display (1), explicit invariant matrix product' -Parent 'NOE-P03-KO-U02-UNIT-001' -Order 4 -Unit 'U02' `
    -SourceStart 3591 -SourceEnd 3594 -TargetStart 17 -TargetEnd 20 -Basis @('source_fact','computation','producer_editorial_inference') `
    -Relations @('equation_for|NOE-P03-KO-U02-THEOREM-003'))
Add-LineFormula -Parent 'NOE-P03-KO-U02-DISPLAY-001' -Order 1 -Unit 'U02' -SourceLine 3592 -TargetLine 18 -Label 'Display (1) paired-expression line'
Add-LineFormula -Parent 'NOE-P03-KO-U02-DISPLAY-001' -Order 2 -Unit 'U02' -SourceLine 3593 -TargetLine 19 -Label 'Display (1) lambda range line'

# U03 converse, display (2), decomposition identity, and concluding theorem.
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-PARAGRAPH-001' -Type 'paragraph' -Label 'Converse explicit-representation claim and identity construction' -Parent 'NOE-P03-KO-U03-UNIT-001' -Order 1 -Unit 'U03' `
    -SourceStart 3596 -SourceEnd 3596 -TargetStart 14 -TargetEnd 14 -Basis @('source_fact','producer_editorial_inference'))
$u03p1Labels = @(
    'Converse explicit matrix-product representation claim',
    'Need to transfer the second symbolic theorem to the n-ary domain',
    'Derivation of identities from x- and u-row identities',
    'Arrival at two dual formulas and lead-in to one display'
)
for ($i = 0; $i -lt $u03p1Labels.Count; $i++) {
    Add-Spec (New-Spec -Id ('NOE-P03-KO-U03-CLOSED-PROSE-{0:D3}' -f ($i + 1)) -Type 'closed_prose' -Label $u03p1Labels[$i] `
        -Parent 'NOE-P03-KO-U03-PARAGRAPH-001' -Order ($i + 1) -Unit 'U03' -SourceStart 3596 -SourceEnd 3596 -TargetStart 14 -TargetEnd 14 `
        -Basis @('producer_editorial_inference'))
}
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-THEOREM-001' -Type 'theorem' -Label 'All invariant formations admit explicit matrix-product representation' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-001' -Order 1 -Unit 'U03' `
    -SourceStart 3596 -SourceEnd 3596 -TargetStart 14 -TargetEnd 14 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U03-PARAGRAPH-001'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-PROOF-001' -Type 'proof' -Label 'Proof strategy by independent indecomposable identities and matrix product laws' -Parent 'NOE-P03-KO-U03-PARAGRAPH-001' -Order 5 -Unit 'U03' `
    -SourceStart 3596 -SourceEnd 3596 -TargetStart 14 -TargetEnd 14 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('proves|NOE-P03-KO-U03-THEOREM-001'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-FOOTNOTE-001' -Type 'footnote' -Label 'Pascal reference for identities containing x and u rows' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-003' -Order 1 -Unit 'U03' `
    -SourceStart 3596 -SourceEnd 3596 -TargetStart 14 -TargetEnd 14 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('note_for|NOE-P03-KO-U03-PROOF-001'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-BIBLIOGRAPHY-ITEM-001' -Type 'bibliography_item' -Label 'E. Pascal, Memorie della R. Accademia dei Lincei (1888)' -Parent 'NOE-P03-KO-U03-FOOTNOTE-001' -Order 1 -Unit 'U03' `
    -SourceStart 3596 -SourceEnd 3596 -TargetStart 14 -TargetEnd 14 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('bibliography_for|NOE-P03-KO-U03-FOOTNOTE-001'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U03-OTHER-001' -Parent 'NOE-P03-KO-U03-PARAGRAPH-001' -Order 6 -Unit 'U03' -SourceLine 3596 -TargetLine 14 -Label 'Converse-proof paragraph inline-math occurrence group'
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-DISPLAY-001' -Type 'display' -Label 'Numbered display (2), dualistic identity' -Parent 'NOE-P03-KO-U03-UNIT-001' -Order 2 -Unit 'U03' `
    -SourceStart 3597 -SourceEnd 3603 -TargetStart 15 -TargetEnd 21 -Basis @('source_fact','computation','producer_editorial_inference') `
    -Relations @('equation_for|NOE-P03-KO-U03-THEOREM-001'))
Add-LineFormula -Parent 'NOE-P03-KO-U03-DISPLAY-001' -Order 1 -Unit 'U03' -SourceLine 3599 -TargetLine 17 -Label 'Display (2) paired-expression left line'
Add-LineFormula -Parent 'NOE-P03-KO-U03-DISPLAY-001' -Order 2 -Unit 'U03' -SourceLine 3600 -TargetLine 18 -Label 'Display (2) summation identity line'
Add-LineFormula -Parent 'NOE-P03-KO-U03-DISPLAY-001' -Order 3 -Unit 'U03' -SourceLine 3601 -TargetLine 19 -Label 'Display (2) rho and sign constraints'

Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-PARAGRAPH-002' -Type 'paragraph' -Label 'Decomposition identity and explicit-representation conclusion' -Parent 'NOE-P03-KO-U03-UNIT-001' -Order 3 -Unit 'U03' `
    -SourceStart 3605 -SourceEnd 3605 -TargetStart 23 -TargetEnd 23 -Basis @('source_fact','producer_editorial_inference'))
$u03p2Labels = @(
    'Unavoidable specialization involving an x row',
    'General symbol and variable rows yield a decomposition identity',
    'Clebsch use of a special decomposition identity',
    'Conclusion that matrix representation supplies explicit symbolic representation'
)
for ($i = 0; $i -lt $u03p2Labels.Count; $i++) {
    Add-Spec (New-Spec -Id ('NOE-P03-KO-U03-CLOSED-PROSE-{0:D3}' -f ($i + 5)) -Type 'closed_prose' -Label $u03p2Labels[$i] `
        -Parent 'NOE-P03-KO-U03-PARAGRAPH-002' -Order ($i + 1) -Unit 'U03' -SourceStart 3605 -SourceEnd 3605 -TargetStart 23 -TargetEnd 23 `
        -Basis @('producer_editorial_inference'))
}
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-DEFINITION-001' -Type 'definition' -Label 'Decomposition identity as splitting a p-rho row into individual x rows' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-006' -Order 1 -Unit 'U03' `
    -SourceStart 3605 -SourceEnd 3605 -TargetStart 23 -TargetEnd 23 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-BIBLIOGRAPHY-ITEM-002' -Type 'bibliography_item' -Label 'Clebsch, Fundamentalaufgabe der Invariantentheorie' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-007' -Order 1 -Unit 'U03' `
    -SourceStart 3605 -SourceEnd 3605 -TargetStart 23 -TargetEnd 23 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('cites|NOE-P03-KO-U03-CLOSED-PROSE-007'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-PROOF-002' -Type 'proof' -Label 'Conclusion mediated by decomposition identities' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-008' -Order 1 -Unit 'U03' `
    -SourceStart 3605 -SourceEnd 3605 -TargetStart 23 -TargetEnd 23 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('proves|NOE-P03-KO-U03-THEOREM-001'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U03-OTHER-002' -Parent 'NOE-P03-KO-U03-PARAGRAPH-002' -Order 5 -Unit 'U03' -SourceLine 3605 -TargetLine 23 -Label 'Decomposition-identity paragraph inline-math occurrence group'

Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-PARAGRAPH-003' -Type 'paragraph' -Label 'Final contraction theorem and proof transfer' -Parent 'NOE-P03-KO-U03-UNIT-001' -Order 4 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference'))
$u03p3Labels = @(
    'Analogous contraction theorem and reduction consequences',
    'Defect and cogredience conditions and theorem statement',
    'Proof dependence on replacement by normal forms',
    'Mertens result in the quaternary domain',
    'Transfer of the Mertens proof to the n-ary domain'
)
for ($i = 0; $i -lt $u03p3Labels.Count; $i++) {
    Add-Spec (New-Spec -Id ('NOE-P03-KO-U03-CLOSED-PROSE-{0:D3}' -f ($i + 9)) -Type 'closed_prose' -Label $u03p3Labels[$i] `
        -Parent 'NOE-P03-KO-U03-PARAGRAPH-003' -Order ($i + 1) -Unit 'U03' -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 `
        -Basis @('producer_editorial_inference'))
}
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-CROSS-REFERENCE-001' -Type 'cross_reference' -Label 'Reference to numbered display (1)' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-010' -Order 1 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','computation','producer_editorial_inference') `
    -Relations @('cross_reference|NOE-P03-KO-U02-DISPLAY-001'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-DEFINITION-002' -Type 'definition' -Label 'Defect of a contraction as lambda in display (1)' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-010' -Order 2 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('cross_reference|NOE-P03-KO-U02-DISPLAY-001'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-DEFINITION-003' -Type 'definition' -Label 'Cogredient contractions as sigma equal to tau' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-010' -Order 3 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-THEOREM-002' -Type 'theorem' -Label 'All contractions generated successively by cogredient contractions of defect one' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-010' -Order 4 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('statement_of|NOE-P03-KO-U03-PARAGRAPH-003'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-DEFINITION-004' -Type 'definition' -Label 'Normal forms annihilated by all invariant differential operations' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-011' -Order 1 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-FOOTNOTE-002' -Type 'footnote' -Label 'Mertens reference for invariant constructions of quaternary forms' -Parent 'NOE-P03-KO-U03-CLOSED-PROSE-012' -Order 1 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('note_for|NOE-P03-KO-U03-PROOF-003'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-BIBLIOGRAPHY-ITEM-003' -Type 'bibliography_item' -Label 'Mertens, Über invariante Gebilde quaternärer Formen, Wiener Berichte 98 (1889)' -Parent 'NOE-P03-KO-U03-FOOTNOTE-002' -Order 1 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('bibliography_for|NOE-P03-KO-U03-FOOTNOTE-002'))
Add-Spec (New-Spec -Id 'NOE-P03-KO-U03-PROOF-003' -Type 'proof' -Label 'Proof outline via normal forms, differential operations, and the decomposition identity' -Parent 'NOE-P03-KO-U03-PARAGRAPH-003' -Order 6 -Unit 'U03' `
    -SourceStart 3607 -SourceEnd 3607 -TargetStart 25 -TargetEnd 25 -Basis @('source_fact','producer_editorial_inference') `
    -Relations @('proves|NOE-P03-KO-U03-THEOREM-002','cites|NOE-P03-KO-U03-BIBLIOGRAPHY-ITEM-003'))
Add-InlineMathGroup -GroupId 'NOE-P03-KO-U03-OTHER-003' -Parent 'NOE-P03-KO-U03-PARAGRAPH-003' -Order 7 -Unit 'U03' -SourceLine 3607 -TargetLine 25 -Label 'Final theorem paragraph inline-math occurrence group'

# Bind and verify all fixed inputs before writing generated artifacts.
$sourceHashActual = Get-FileSha256 $sourcePath
if ($sourceHashActual -ne $sourceHashExpected) { throw "Authority hash mismatch: $sourceHashActual" }
$paperInterval = Get-LfSliceInfo $sourcePath 3573 3608
if ($paperInterval.sha256 -ne $paperIntervalHashExpected -or $paperInterval.bytes -ne 8277) {
    throw "Paper 3 interval identity mismatch: $($paperInterval.sha256) / $($paperInterval.bytes)"
}

$targetHashActual = [ordered]@{}
foreach ($unit in $targets.Keys) {
    $targetHashActual[$unit] = Get-FileSha256 $targets[$unit]
    if ($targetHashActual[$unit] -ne $targetHashExpected[$unit]) { throw "Target hash mismatch for $unit" }
    $sourceSlice = Get-LfSliceInfo $sourcePath $unitSource[$unit].start $unitSource[$unit].end
    if ($sourceSlice.sha256 -ne $unitSource[$unit].sha256 -or $sourceSlice.bytes -ne $unitSource[$unit].bytes) {
        throw "Source unit identity mismatch for $unit"
    }
}

function New-SourceLocator([object]$Spec) {
    $slice = Get-LfSliceInfo $sourcePath $Spec.source_start $Spec.source_end
    $fragmentKind = if ($null -ne $Spec.source_fragment) { 'inline_math' } else { 'line_slice' }
    return [ordered]@{
        path = $sourcePath
        line_start = $Spec.source_start
        line_end = $Spec.source_end
        file_sha256 = $sourceHashActual
        slice_sha256_lf = $slice.sha256
        fragment_kind = $fragmentKind
        fragment_occurrence = $Spec.source_occurrence
        fragment_text = $Spec.source_fragment
        fragment_sha256_utf8 = Get-Utf8Sha256 $Spec.source_fragment
    }
}

function New-TargetLocator([string]$Unit, [int]$Start, [int]$End, [AllowNull()][object]$Fragment, [AllowNull()][object]$Occurrence) {
    $path = $targets[$Unit]
    $slice = Get-LfSliceInfo $path $Start $End
    $fragmentKind = if ($null -ne $Fragment) { 'inline_math' } else { 'line_slice' }
    return [ordered]@{
        unit_id = $Unit
        path = $path
        line_start = $Start
        line_end = $End
        file_sha256 = $targetHashActual[$Unit]
        slice_sha256_lf = $slice.sha256
        fragment_kind = $fragmentKind
        fragment_occurrence = $Occurrence
        fragment_text = $Fragment
        fragment_sha256_utf8 = Get-Utf8Sha256 $Fragment
    }
}

$records = [System.Collections.Generic.List[object]]::new()
foreach ($spec in $specs) {
    $relations = [System.Collections.Generic.List[object]]::new()
    if ($null -ne $spec.parent) {
        [void]$relations.Add([ordered]@{ relation = 'embedded_in'; target_id = $spec.parent })
    }
    foreach ($relationSpec in $spec.relations) {
        $parts = $relationSpec -split '\|', 2
        if ($parts.Count -ne 2) { throw "Invalid relation specification: $relationSpec" }
        [void]$relations.Add([ordered]@{ relation = $parts[0]; target_id = $parts[1] })
    }

    $targetLocators = [System.Collections.Generic.List[object]]::new()
    if ($spec.unit -eq 'ALL') {
        foreach ($unit in $targets.Keys) {
            [void]$targetLocators.Add((New-TargetLocator $unit $unitTargetBody[$unit][0] $unitTargetBody[$unit][1] $null $null))
        }
    }
    else {
        [void]$targetLocators.Add((New-TargetLocator $spec.unit $spec.target_start $spec.target_end $spec.target_fragment $spec.target_occurrence))
    }

    $baseRecord = [ordered]@{
        schema_version = '1.2'
        record_id = $spec.id
        work_id = 'NOE-P03'
        unit_id = $spec.unit
        structure_type = $spec.type
        label = $spec.label
        parent_id = $spec.parent
        order = $spec.order
        record_basis = @($spec.basis)
        source_language = 'de'
        target_language = 'ko-KR'
        authority_pointer = [ordered]@{ pointer_id = $pointerId; pointer_sha256 = $pointerHash }
        authority_state = 'current_v003_translation_input_unchecked'
        source_locator = New-SourceLocator $spec
        target_locators = @($targetLocators)
        relations = @($relations)
        completion_state = 'producer_draft_text_covered'
        review_state = 'unchecked'
        publication_state = 'private_not_for_publication'
        continuation_cursor = $unitCursor[$spec.unit]
    }
    $canonical = $baseRecord | ConvertTo-Json -Compress -Depth 20
    $baseRecord.record_sha256 = Get-Utf8Sha256 $canonical
    [void]$records.Add([pscustomobject]$baseRecord)
}

$jsonlPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.jsonl'
$csvPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.csv'
$jsonLines = @($records | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 20 })
[System.IO.File]::WriteAllText($jsonlPath, ([string]::Join("`n", $jsonLines) + "`n"), $utf8NoBom)

function ConvertTo-CsvField([AllowNull()][object]$Value) {
    $text = if ($null -eq $Value) { '' } else { [string]$Value }
    return '"' + $text.Replace('"', '""') + '"'
}

$csvHeaders = @(
    'schema_version','record_id','work_id','unit_id','structure_type','label','parent_id','order',
    'record_basis_json','source_language','target_language','authority_pointer_id','authority_pointer_sha256','authority_state',
    'source_path','source_line_start','source_line_end','source_file_sha256','source_slice_sha256_lf',
    'source_fragment_kind','source_fragment_occurrence','source_fragment_text','source_fragment_sha256_utf8',
    'target_locator_count','target_paths','target_file_sha256_values','target_locators_json','relations_json',
    'completion_state','review_state','publication_state','continuation_cursor','record_sha256'
)
$csvLines = [System.Collections.Generic.List[string]]::new()
[void]$csvLines.Add(($csvHeaders | ForEach-Object { ConvertTo-CsvField $_ }) -join ',')
foreach ($record in $records) {
    $targetPaths = @($record.target_locators | ForEach-Object { $_.path }) -join ';'
    $targetHashes = @($record.target_locators | ForEach-Object { $_.file_sha256 }) -join ';'
    $values = @(
        $record.schema_version, $record.record_id, $record.work_id, $record.unit_id, $record.structure_type, $record.label,
        $record.parent_id, $record.order, ($record.record_basis | ConvertTo-Json -Compress), $record.source_language,
        $record.target_language, $record.authority_pointer.pointer_id, $record.authority_pointer.pointer_sha256,
        $record.authority_state, $record.source_locator.path, $record.source_locator.line_start, $record.source_locator.line_end,
        $record.source_locator.file_sha256, $record.source_locator.slice_sha256_lf, $record.source_locator.fragment_kind,
        $record.source_locator.fragment_occurrence, $record.source_locator.fragment_text, $record.source_locator.fragment_sha256_utf8,
        $record.target_locators.Count, $targetPaths, $targetHashes,
        ($record.target_locators | ConvertTo-Json -Compress -Depth 10),
        ($record.relations | ConvertTo-Json -Compress -Depth 10),
        $record.completion_state, $record.review_state, $record.publication_state, $record.continuation_cursor, $record.record_sha256
    )
    [void]$csvLines.Add(($values | ForEach-Object { ConvertTo-CsvField $_ }) -join ',')
}
[System.IO.File]::WriteAllText($csvPath, ([string]::Join("`n", $csvLines) + "`n"), $utf8NoBom)

$result = [ordered]@{
    status = 'built'
    record_count = $records.Count
    latest_record_id = $records[$records.Count - 1].record_id
    jsonl_sha256 = Get-FileSha256 $jsonlPath
    csv_sha256 = Get-FileSha256 $csvPath
}
Write-Output ($result | ConvertTo-Json -Compress)
