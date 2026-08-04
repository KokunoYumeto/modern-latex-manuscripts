$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$indexDir = $PSScriptRoot
$root = (Resolve-Path -LiteralPath (Join-Path $indexDir '..\..')).Path
$sourcePath = 'C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper41_zh_translation_001_20260722\source\Noether_Paper41_CurrentGermanAuthority_interval.tex'
$expectedSourceFileHash = 'C265058425E5E2D1A2289CC03A9DDEDDDF4803A3215DC3F173B93E7AB69D60ED'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$unitSourceLines = [ordered]@{
    U01 = @(1, 11)
    U02 = @(13, 20)
    U03 = @(22, 46)
    U04 = @(48, 56)
    U05 = @(58, 66)
    U06 = @(68, 78)
    U07 = @(80, 95)
    U08 = @(97, 105)
    U09 = @(107, 120)
    U10 = @(122, 129)
    U11 = @(131, 143)
    U12 = @(145, 151)
}
$expectedUnitSourceHash = [ordered]@{
    U01 = 'BAD33EF459284C4E06A877CEBD624F8C843DED51B82A608475F7FB9726F0228C'
    U02 = '8C0BC86950AD752B9CAED52C54765F6AF6E3592D48996200313845B44942F6BD'
    U03 = 'E1509DFE9ED80F79ED65F770EABF148C56CB853B2E7BD075E629175E2D426EFD'
    U04 = 'F0D1FF2818BD95257249E93DB56E891343DF2EB025DD3F46987461ACCA05A0FC'
    U05 = 'BCEA8450C5DC412DA1506DD0A8A935AD5517D2B03637C57698B6C3D504FB7788'
    U06 = '1EC47AC260130703D0C0313186283365D339F04472184000D219ED44962EA55D'
    U07 = '6B1BAB1A613156C833C091DFE9C98D8C63610545811F24A5E27EF65FE9751A15'
    U08 = '1432D5DDE7E39212CE1D1EC7478348C0856AEB80A6D4FB7324954781A3075BF5'
    U09 = '78A0D977D2F04C537D3DFD91AA23ED2F221EBDA5D5A4A8F8081EA0CFCB93520F'
    U10 = 'D31F076B49A420DB830B465D325C4360EA283D3B6A23CE67E2416AC225FAEC24'
    U11 = '6F8C5A72030ED3C658C0C0CA0D99077E88F9C4B967BEA672D1F3CE148DE1C2F9'
    U12 = 'D0259D62D1D60476EE3F16E2E22BDFB8CDAD7A4978DC12683A5C0999AEA4DDBE'
}
$unitCursor = [ordered]@{
    U01 = 'continue at Paper 41 snapshot line 13 / Korean U02'
    U02 = 'continue at Paper 41 snapshot line 22 / Korean U03'
    U03 = 'continue at Paper 41 snapshot line 48 / Korean U04'
    U04 = 'continue at Paper 41 snapshot line 58 / Korean U05'
    U05 = 'continue at Paper 41 snapshot line 68 / Korean U06'
    U06 = 'continue at Paper 41 snapshot line 80 / Korean U07'
    U07 = 'continue at Paper 41 snapshot line 97 / Korean U08'
    U08 = 'continue at Paper 41 snapshot line 107 / Korean U09'
    U09 = 'continue at Paper 41 snapshot line 122 / Korean U10'
    U10 = 'continue at Paper 41 snapshot line 131 / Korean U11'
    U11 = 'continue at Paper 41 snapshot line 145 / Korean U12'
    U12 = 'Paper 41 substantive interval exhausted at line 151; source controls 153--154 excluded; await independent Korean checker'
}
$targets = [ordered]@{}
foreach ($number in 1..12) {
    $unit = 'U{0:D2}' -f $number
    $targets[$unit] = Join-Path $root ('targets\Noether_P41_Korean_{0}_UNCHECKED.tex' -f $unit)
}

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

function Get-LfSliceSha256([string]$Path, [int]$Start, [int]$End) {
    $lines = [System.IO.File]::ReadAllLines($Path, $utf8NoBom)
    if ($Start -lt 1 -or $End -lt $Start -or $End -gt $lines.Length) {
        throw "Invalid line slice $Start-$End for $Path with $($lines.Length) lines"
    }
    $slice = [string]::Join([char]10, $lines[($Start - 1)..($End - 1)]) + [char]10
    return Get-TextSha256 $slice
}

function Convert-TargetSpec([string]$Spec) {
    $parts = $Spec.Split(':')
    if ($parts.Count -ne 3) {
        throw "Invalid target specification: $Spec"
    }
    $unit = $parts[0]
    if (-not $targets.Contains($unit)) {
        throw "Unknown target unit in specification: $Spec"
    }
    return [pscustomobject]@{
        unit = $unit
        line_start = [int]$parts[1]
        line_end = [int]$parts[2]
    }
}

function Convert-RelationSpec([string]$Spec) {
    $separator = $Spec.IndexOf(':')
    if ($separator -lt 1) {
        throw "Invalid relation specification: $Spec"
    }
    return [pscustomobject]@{
        relation = $Spec.Substring(0, $separator)
        target_id = $Spec.Substring($separator + 1)
    }
}

# Columns:
# record_id | structure_type | label | parent_id | order | source_line_start |
# source_line_end | comma-separated UNIT:START:END targets |
# comma-separated RELATION:TARGET_ID relations.
# Structural pairing and labels are producer editorial metadata only.
$manifestText = @'
NOE-P41-KO-WORK-001|work|Paper 41 complete substantive translated interval||1|1|151|U01:11:21,U02:11:18,U03:11:35,U04:11:19,U05:11:19,U06:11:21,U07:11:26,U08:11:19,U09:12:25,U10:12:19,U11:12:24,U12:12:18|contains:NOE-P41-KO-U01,contains:NOE-P41-KO-U02,contains:NOE-P41-KO-U03,contains:NOE-P41-KO-U04,contains:NOE-P41-KO-U05,contains:NOE-P41-KO-U06,contains:NOE-P41-KO-U07,contains:NOE-P41-KO-U08,contains:NOE-P41-KO-U09,contains:NOE-P41-KO-U10,contains:NOE-P41-KO-U11,contains:NOE-P41-KO-U12
NOE-P41-KO-U01|unit|Title and introduction|NOE-P41-KO-WORK-001|1|1|11|U01:11:21|
NOE-P41-KO-U02|unit|Minimal theorem setup and crossed-product introduction|NOE-P41-KO-WORK-001|2|13|20|U02:11:18|continues:NOE-P41-KO-U01
NOE-P41-KO-U03|unit|Crossed-product relations and Brauer classes|NOE-P41-KO-WORK-001|3|22|46|U03:11:35|continues:NOE-P41-KO-U02
NOE-P41-KO-U04|unit|Cyclic-algebra specialization|NOE-P41-KO-WORK-001|4|48|56|U04:11:19|continues:NOE-P41-KO-U03
NOE-P41-KO-U05|unit|Extension group and three minimal formulations|NOE-P41-KO-WORK-001|5|58|66|U05:11:19|continues:NOE-P41-KO-U04
NOE-P41-KO-U06|unit|Proof of minimal theorem and Schur-index generalization|NOE-P41-KO-WORK-001|6|68|78|U06:11:21|continues:NOE-P41-KO-U05
NOE-P41-KO-U07|unit|Class partitions and induced factor-system class definition|NOE-P41-KO-WORK-001|7|80|95|U07:11:26|continues:NOE-P41-KO-U06
NOE-P41-KO-U08|unit|Three principal-genus theorem formulations|NOE-P41-KO-WORK-001|8|97|105|U08:11:19|continues:NOE-P41-KO-U07
NOE-P41-KO-U09|unit|Proof opening and two auxiliary lemmas|NOE-P41-KO-WORK-001|9|107|120|U09:12:25|continues:NOE-P41-KO-U08
NOE-P41-KO-U10|unit|Local decomposition and unramified setup|NOE-P41-KO-WORK-001|10|122|129|U10:12:19|continues:NOE-P41-KO-U09
NOE-P41-KO-U11|unit|Normalized cyclic representation and auxiliary-lemma conclusion|NOE-P41-KO-WORK-001|11|131|143|U11:12:24|continues:NOE-P41-KO-U10
NOE-P41-KO-U12|unit|Final proof, cyclic specialization, and receipt|NOE-P41-KO-WORK-001|12|145|151|U12:12:18|continues:NOE-P41-KO-U11
NOE-P41-KO-U01-TITLE-001|title|Paper title|NOE-P41-KO-U01|1|1|1|U01:11:11|
NOE-P41-KO-U01-AUTHOR-001|author|Emmy Noether byline|NOE-P41-KO-U01|2|3|5|U01:13:15|
NOE-P41-KO-U01-PUBLICATION-001|publication_note|Math. Ann. 108 publication citation|NOE-P41-KO-U01|3|6|6|U01:16:16|
NOE-P41-KO-U01-PARA-001|paragraph|Noncommutative methods and theorem motivation|NOE-P41-KO-U01|4|9|9|U01:19:19|
NOE-P41-KO-U01-NOTE-001|footnote|Zurich lecture and Hasse references|NOE-P41-KO-U01-PARA-001|1|9|9|U01:19:19|note_for:NOE-P41-KO-U01-PARA-001
NOE-P41-KO-U01-BIB-001|bibliography_item|Noether Zurich ICM lecture 1932|NOE-P41-KO-U01-NOTE-001|1|9|9|U01:19:19|bibliography_for:NOE-P41-KO-U01-NOTE-001
NOE-P41-KO-U01-BIB-002|bibliography_item|Hasse Brauer algebra class group 1932|NOE-P41-KO-U01-NOTE-001|2|9|9|U01:19:19|bibliography_for:NOE-P41-KO-U01-NOTE-001
NOE-P41-KO-U01-NOTE-002|footnote|Minimal versus small sense distinction|NOE-P41-KO-U01-PARA-001|2|9|9|U01:19:19|note_for:NOE-P41-KO-U01-PARA-001
NOE-P41-KO-U01-NOTE-003|footnote|Speiser source for the minimal theorem|NOE-P41-KO-U01-PARA-001|3|9|9|U01:19:19|note_for:NOE-P41-KO-U01-PARA-001
NOE-P41-KO-U01-BIB-003|bibliography_item|Speiser group-theoretic number theory 1919|NOE-P41-KO-U01-NOTE-003|1|9|9|U01:19:19|bibliography_for:NOE-P41-KO-U01-NOTE-003
NOE-P41-KO-U01-PARA-002|paragraph|Proof strategy through ideals and maximal orders|NOE-P41-KO-U01|5|11|11|U01:21:21|
NOE-P41-KO-U01-NOTE-004|footnote|Hasse account of Brandt maximal orders|NOE-P41-KO-U01-PARA-002|1|11|11|U01:21:21|note_for:NOE-P41-KO-U01-PARA-002
NOE-P41-KO-U01-BIB-004|bibliography_item|Hasse p-adic division algebras 1931|NOE-P41-KO-U01-NOTE-004|1|11|11|U01:21:21|bibliography_for:NOE-P41-KO-U01-NOTE-004
NOE-P41-KO-U01-NOTE-005|footnote|Forthcoming maximal-order notes|NOE-P41-KO-U01-PARA-002|2|11|11|U01:21:21|note_for:NOE-P41-KO-U01-PARA-002
NOE-P41-KO-U01-BIB-005|bibliography_item|Chevalley forthcoming note|NOE-P41-KO-U01-NOTE-005|1|11|11|U01:21:21|bibliography_for:NOE-P41-KO-U01-NOTE-005
NOE-P41-KO-U01-BIB-006|bibliography_item|Hasse forthcoming Herbrand memorial note|NOE-P41-KO-U01-NOTE-005|2|11|11|U01:21:21|bibliography_for:NOE-P41-KO-U01-NOTE-005
NOE-P41-KO-U01-BIB-007|bibliography_item|Noether forthcoming Herbrand memorial note|NOE-P41-KO-U01-NOTE-005|3|11|11|U01:21:21|bibliography_for:NOE-P41-KO-U01-NOTE-005
NOE-P41-KO-U02-SECTION-001|section_heading|Section 1 marker|NOE-P41-KO-U02|1|13|13|U02:11:11|
NOE-P41-KO-U02-SUBSECTION-001|subsection_heading|Principal genus theorem in the minimal case|NOE-P41-KO-U02|2|14|16|U02:12:14|
NOE-P41-KO-U02-PARA-001|paragraph|Field extension and Galois group setup|NOE-P41-KO-U02|3|18|18|U02:16:16|
NOE-P41-KO-U02-DIVISION-001|division_heading|Part 1 crossed-product facts|NOE-P41-KO-U02|4|20|20|U02:18:18|
NOE-P41-KO-U02-PARA-002|paragraph|Crossed-product embedding and linear-form module|NOE-P41-KO-U02|5|20|20|U02:18:18|
NOE-P41-KO-U02-NOTE-001|footnote|Sources for crossed-product theory|NOE-P41-KO-U02-PARA-002|1|20|20|U02:18:18|note_for:NOE-P41-KO-U02-PARA-002
NOE-P41-KO-U02-BIB-001|bibliography_item|Hasse Theory of cyclic algebras 1932|NOE-P41-KO-U02-NOTE-001|1|20|20|U02:18:18|bibliography_for:NOE-P41-KO-U02-NOTE-001
NOE-P41-KO-U02-BIB-002|bibliography_item|Deuring forthcoming report on hypercomplex numbers|NOE-P41-KO-U02-NOTE-001|2|20|20|U02:18:18|bibliography_for:NOE-P41-KO-U02-NOTE-001
NOE-P41-KO-U02-BIB-003|bibliography_item|Noether Zurich lecture cited again|NOE-P41-KO-U02-NOTE-001|3|20|20|U02:18:18|bibliography_for:NOE-P41-KO-U02-NOTE-001,cites:NOE-P41-KO-U01-BIB-001
NOE-P41-KO-U03-DISPLAY-001|display|Equation 1 crossed-product module|NOE-P41-KO-U03|1|22|22|U03:11:11|equation_for:NOE-P41-KO-U02-PARA-002
NOE-P41-KO-U03-PARA-001|paragraph|Inner-automorphism condition and algebra rank|NOE-P41-KO-U03|2|24|24|U03:13:13|
NOE-P41-KO-U03-NOTE-001|footnote|Definition of K star notation|NOE-P41-KO-U03-PARA-001|1|24|24|U03:13:13|note_for:NOE-P41-KO-U03-PARA-001
NOE-P41-KO-U03-DISPLAY-002|display|Equation 2 inner action relation|NOE-P41-KO-U03-PARA-001|2|26|26|U03:15:15|equation_for:NOE-P41-KO-U03-PARA-001
NOE-P41-KO-U03-PARA-002|paragraph|Quantifier for equation 2 and transition to multiplication|NOE-P41-KO-U03|3|28|28|U03:17:17|
NOE-P41-KO-U03-DISPLAY-003|display|Equation 3 multiplication relation|NOE-P41-KO-U03-PARA-002|1|30|30|U03:19:19|equation_for:NOE-P41-KO-U03-PARA-002
NOE-P41-KO-U03-DISPLAY-004|display|Equation 4 factor-system cocycle relation|NOE-P41-KO-U03-PARA-002|2|32|32|U03:21:21|equation_for:NOE-P41-KO-U03-PARA-002
NOE-P41-KO-U03-REMARK-001|remark|Associativity equivalence|NOE-P41-KO-U03|4|34|34|U03:23:23|cross_reference:NOE-P41-KO-U03-DISPLAY-004
NOE-P41-KO-U03-PARA-003|paragraph|Arbitrary product definition and central-simple algebra consequences|NOE-P41-KO-U03|5|36|40|U03:25:29|
NOE-P41-KO-U03-DISPLAY-005|display|Unnumbered arbitrary-product equation|NOE-P41-KO-U03-PARA-003|1|37|39|U03:26:28|equation_for:NOE-P41-KO-U03-PARA-003
NOE-P41-KO-U03-PARA-004|paragraph|Change of crossed-product generators|NOE-P41-KO-U03|6|42|42|U03:31:31|
NOE-P41-KO-U03-DISPLAY-006|display|Equation 5 associated factor systems|NOE-P41-KO-U03-PARA-004|1|44|44|U03:33:33|equation_for:NOE-P41-KO-U03-PARA-004
NOE-P41-KO-U03-PARA-005|paragraph|Factor-system and algebra class correspondence|NOE-P41-KO-U03|7|46|46|U03:35:35|
NOE-P41-KO-U03-THEOREM-001|theorem|Brauer group statement with fixed splitting field|NOE-P41-KO-U03-PARA-005|1|46|46|U03:35:35|statement_of:NOE-P41-KO-U03-PARA-005
NOE-P41-KO-U04-PARA-001|paragraph|Cyclic-algebra specialization setup|NOE-P41-KO-U04|1|48|48|U04:11:11|
NOE-P41-KO-U04-DISPLAY-001|display|Equation 1 prime cyclic module|NOE-P41-KO-U04-PARA-001|1|50|50|U04:13:13|equation_for:NOE-P41-KO-U04-PARA-001
NOE-P41-KO-U04-DISPLAY-002|display|Equation 2 prime cyclic action|NOE-P41-KO-U04-PARA-001|2|51|51|U04:14:14|equation_for:NOE-P41-KO-U04-PARA-001
NOE-P41-KO-U04-DISPLAY-003|display|Equation 3 prime power relation|NOE-P41-KO-U04-PARA-001|3|52|52|U04:15:15|equation_for:NOE-P41-KO-U04-PARA-001
NOE-P41-KO-U04-DISPLAY-004|display|Equation 4 prime ground-field condition|NOE-P41-KO-U04-PARA-001|4|53|53|U04:16:16|equation_for:NOE-P41-KO-U04-PARA-001
NOE-P41-KO-U04-DISPLAY-005|display|Equation 5 prime norm transformation|NOE-P41-KO-U04-PARA-001|5|54|54|U04:17:17|equation_for:NOE-P41-KO-U04-PARA-001
NOE-P41-KO-U04-PARA-002|paragraph|Cyclic factor systems and quotient group|NOE-P41-KO-U04|2|56|56|U04:19:19|
NOE-P41-KO-U05-DIVISION-001|division_heading|Part 2 minimal theorem formulation|NOE-P41-KO-U05|1|58|58|U05:11:11|
NOE-P41-KO-U05-PARA-001|paragraph|Extension-group construction|NOE-P41-KO-U05|2|58|58|U05:11:11|
NOE-P41-KO-U05-DISPLAY-001|display|Equation 6 extension group|NOE-P41-KO-U05-PARA-001|1|60|60|U05:13:13|equation_for:NOE-P41-KO-U05-PARA-001
NOE-P41-KO-U05-PARA-002|paragraph|Normalizer characterization of the extension group|NOE-P41-KO-U05|3|62|62|U05:15:15|
NOE-P41-KO-U05-NOTE-001|footnote|Group extension versus ring extension|NOE-P41-KO-U05-PARA-002|1|62|62|U05:15:15|note_for:NOE-P41-KO-U05-PARA-002
NOE-P41-KO-U05-THEOREM-001|theorem|Principal genus theorem in the minimal case|NOE-P41-KO-U05|4|64|64|U05:17:17|
NOE-P41-KO-U05-FORMULATION-001|formulation|Minimal theorem first formulation|NOE-P41-KO-U05-THEOREM-001|1|64|64|U05:17:17|statement_of:NOE-P41-KO-U05-THEOREM-001
NOE-P41-KO-U05-FORMULATION-002|formulation|Minimal theorem second formulation|NOE-P41-KO-U05-THEOREM-001|2|64|64|U05:17:17|statement_of:NOE-P41-KO-U05-THEOREM-001
NOE-P41-KO-U05-FORMULATION-003|formulation|Minimal theorem third formulation|NOE-P41-KO-U05-THEOREM-001|3|64|64|U05:17:17|statement_of:NOE-P41-KO-U05-THEOREM-001
NOE-P41-KO-U05-DEFINITION-001|definition|Crossed representation and equivalence class|NOE-P41-KO-U05|5|66|66|U05:19:19|
NOE-P41-KO-U06-PROOF-001|proof|Proof of the three minimal formulations|NOE-P41-KO-U05-THEOREM-001|1|68|76|U06:11:19|proves:NOE-P41-KO-U05-THEOREM-001
NOE-P41-KO-U06-PROOF-STEP-001|proof_step|Extension from group to ring automorphism|NOE-P41-KO-U06-PROOF-001|1|68|68|U06:11:11|
NOE-P41-KO-U06-PROOF-STEP-002|proof_step|Equivalence of first and second formulations|NOE-P41-KO-U06-PROOF-001|2|70|74|U06:13:17|
NOE-P41-KO-U06-DISPLAY-001|display|Inner-automorphism coboundary equation|NOE-P41-KO-U06-PROOF-STEP-002|1|71|73|U06:14:16|equation_for:NOE-P41-KO-U06-PROOF-STEP-002
NOE-P41-KO-U06-NOTE-001|footnote|Finite-field scope of the proof|NOE-P41-KO-U06-PROOF-STEP-002|2|74|74|U06:17:17|note_for:NOE-P41-KO-U06-PROOF-STEP-002
NOE-P41-KO-U06-PROOF-STEP-003|proof_step|Equivalence of second and third formulations|NOE-P41-KO-U06-PROOF-001|3|76|76|U06:19:19|
NOE-P41-KO-U06-THEOREM-001|theorem|Unique irreducible crossed representation class|NOE-P41-KO-U06|2|78|78|U06:21:21|
NOE-P41-KO-U06-NOTE-002|footnote|Schur-index and representation-module references|NOE-P41-KO-U06-THEOREM-001|1|78|78|U06:21:21|note_for:NOE-P41-KO-U06-THEOREM-001
NOE-P41-KO-U06-BIB-001|bibliography_item|Schur remarks on Speiser 1919|NOE-P41-KO-U06-NOTE-002|1|78|78|U06:21:21|bibliography_for:NOE-P41-KO-U06-NOTE-002
NOE-P41-KO-U06-BIB-002|bibliography_item|Deuring report cited for a module proof|NOE-P41-KO-U06-NOTE-002|2|78|78|U06:21:21|bibliography_for:NOE-P41-KO-U06-NOTE-002,cites:NOE-P41-KO-U02-BIB-002
NOE-P41-KO-U07-SECTION-001|section_heading|Section 2 marker|NOE-P41-KO-U07|1|80|80|U07:11:11|
NOE-P41-KO-U07-SUBSECTION-001|subsection_heading|The principal genus theorem|NOE-P41-KO-U07|2|81|83|U07:12:14|
NOE-P41-KO-U07-DIVISION-001|division_heading|Part 1 preliminary remarks on class partition|NOE-P41-KO-U07|3|85|85|U07:16:16|
NOE-P41-KO-U07-PARA-001|paragraph|Absolute ideal classes and ray classes|NOE-P41-KO-U07|4|85|85|U07:16:16|
NOE-P41-KO-U07-PARA-002|paragraph|Extension to absolute ideal classes and induced equivalence|NOE-P41-KO-U07|5|87|87|U07:18:18|
NOE-P41-KO-U07-NOTE-001|footnote|General invariant subgroup as principal class|NOE-P41-KO-U07-PARA-002|1|87|87|U07:18:18|note_for:NOE-P41-KO-U07-PARA-002
NOE-P41-KO-U07-THEOREM-001|theorem|Criterion for unique product relations on ideal classes|NOE-P41-KO-U07|6|89|89|U07:20:20|
NOE-P41-KO-U07-TRANSITION-001|transition|Transition to ray-class generalization|NOE-P41-KO-U07|7|91|91|U07:22:22|
NOE-P41-KO-U07-DEFINITION-001|definition|Induced ideal-class partition of factor systems|NOE-P41-KO-U07|8|93|93|U07:24:24|
NOE-P41-KO-U07-PARA-003|paragraph|Group property of the defined principal ideals|NOE-P41-KO-U07|9|95|95|U07:26:26|
NOE-P41-KO-U08-DIVISION-001|division_heading|Part 2 formulation of the principal genus theorem|NOE-P41-KO-U08|1|97|97|U08:11:11|
NOE-P41-KO-U08-PARA-001|paragraph|Announcement of three equivalent formulations|NOE-P41-KO-U08|2|97|97|U08:11:11|
NOE-P41-KO-U08-THEOREM-001|theorem|Principal genus theorem|NOE-P41-KO-U08|3|99|103|U08:13:17|
NOE-P41-KO-U08-FORMULATION-001|formulation|Principal genus theorem first formulation|NOE-P41-KO-U08-THEOREM-001|1|99|99|U08:13:13|statement_of:NOE-P41-KO-U08-THEOREM-001
NOE-P41-KO-U08-NOTE-001|footnote|Ideal-class bar notation|NOE-P41-KO-U08-FORMULATION-001|1|99|99|U08:13:13|note_for:NOE-P41-KO-U08-FORMULATION-001
NOE-P41-KO-U08-FORMULATION-002|formulation|Principal genus theorem second formulation|NOE-P41-KO-U08-THEOREM-001|2|101|101|U08:15:15|statement_of:NOE-P41-KO-U08-THEOREM-001
NOE-P41-KO-U08-FORMULATION-003|formulation|Principal genus theorem third formulation|NOE-P41-KO-U08-THEOREM-001|3|103|103|U08:17:17|statement_of:NOE-P41-KO-U08-THEOREM-001
NOE-P41-KO-U08-REMARK-001|remark|Equivalence, ambiguous classes, and representation matrices|NOE-P41-KO-U08|4|105|105|U08:19:19|cross_reference:NOE-P41-KO-U08-THEOREM-001
NOE-P41-KO-U09-DIVISION-001|division_heading|Part 3 proof of the principal genus theorem|NOE-P41-KO-U09|1|107|107|U09:12:12|
NOE-P41-KO-U09-PARA-001|paragraph|Proof plan through two auxiliary lemmas|NOE-P41-KO-U09|2|107|107|U09:12:12|
NOE-P41-KO-U09-LEMMA-001|lemma|Auxiliary lemma 1 principal genus theorem for ideals|NOE-P41-KO-U09|3|109|109|U09:14:14|
NOE-P41-KO-U09-PROOF-001|proof|Proof of auxiliary lemma 1|NOE-P41-KO-U09-LEMMA-001|1|111|118|U09:16:23|proves:NOE-P41-KO-U09-LEMMA-001
NOE-P41-KO-U09-NOTE-001|footnote|Cross-reference to the introduction conclusion|NOE-P41-KO-U09-PROOF-001|1|111|111|U09:16:16|note_for:NOE-P41-KO-U09-PROOF-001
NOE-P41-KO-U09-DISPLAY-001|display|Ideal module-sum proof equations|NOE-P41-KO-U09-PROOF-001|2|112|118|U09:17:23|equation_for:NOE-P41-KO-U09-PROOF-001
NOE-P41-KO-U09-LEMMA-002|lemma|Auxiliary lemma 2 alternate splitting-algebra theorem|NOE-P41-KO-U09|4|120|120|U09:25:25|
NOE-P41-KO-U09-NOTE-002|footnote|Element-level strengthening of auxiliary lemma 2|NOE-P41-KO-U09-LEMMA-002|1|120|120|U09:25:25|note_for:NOE-P41-KO-U09-LEMMA-002
NOE-P41-KO-U10-PROOF-001|proof|Proof of auxiliary lemma 2, local setup|NOE-P41-KO-U09-LEMMA-002|2|122|129|U10:12:19|proves:NOE-P41-KO-U09-LEMMA-002
NOE-P41-KO-U10-PARA-001|paragraph|p-adic extension and decomposition-group setup|NOE-P41-KO-U10-PROOF-001|1|122|122|U10:12:12|
NOE-P41-KO-U10-DISPLAY-001|display|Local algebra similarity relation|NOE-P41-KO-U10-PROOF-001|2|123|125|U10:13:15|equation_for:NOE-P41-KO-U10-PROOF-001
NOE-P41-KO-U10-NOTE-001|footnote|Proof and references for the local similarity relation|NOE-P41-KO-U10-DISPLAY-001|1|124|124|U10:14:14|note_for:NOE-P41-KO-U10-DISPLAY-001
NOE-P41-KO-U10-BIB-001|bibliography_item|Hasse cyclic algebras section 14|NOE-P41-KO-U10-NOTE-001|1|124|124|U10:14:14|bibliography_for:NOE-P41-KO-U10-NOTE-001,cites:NOE-P41-KO-U02-BIB-001
NOE-P41-KO-U10-BIB-002|bibliography_item|van der Waerden volume II page 210|NOE-P41-KO-U10-NOTE-001|2|124|124|U10:14:14|bibliography_for:NOE-P41-KO-U10-NOTE-001
NOE-P41-KO-U10-BIB-003|bibliography_item|Noether forthcoming noncommutative algebra paper|NOE-P41-KO-U10-NOTE-001|3|124|124|U10:14:14|bibliography_for:NOE-P41-KO-U10-NOTE-001
NOE-P41-KO-U10-PARA-002|paragraph|Unramified inertia-field representation|NOE-P41-KO-U10-PROOF-001|3|127|127|U10:17:17|
NOE-P41-KO-U10-NOTE-002|footnote|Hasse reference for the inertia field|NOE-P41-KO-U10-PARA-002|1|127|127|U10:17:17|note_for:NOE-P41-KO-U10-PARA-002
NOE-P41-KO-U10-BIB-004|bibliography_item|Hasse p-adic division algebras section 3|NOE-P41-KO-U10-NOTE-002|1|127|127|U10:17:17|bibliography_for:NOE-P41-KO-U10-NOTE-002,cites:NOE-P41-KO-U01-BIB-004
NOE-P41-KO-U10-PARA-003|paragraph|Reduction to a unit-valued factor system|NOE-P41-KO-U10-PROOF-001|4|129|129|U10:19:19|
NOE-P41-KO-U11-PROOF-002|proof|Proof of auxiliary lemma 2, cyclic normalization and conclusion|NOE-P41-KO-U09-LEMMA-002|3|131|143|U11:12:24|proves:NOE-P41-KO-U09-LEMMA-002,continues:NOE-P41-KO-U10-PROOF-001
NOE-P41-KO-U11-PARA-001|paragraph|Preservation under normalized cyclic representation|NOE-P41-KO-U11-PROOF-002|1|131|131|U11:12:12|
NOE-P41-KO-U11-DISPLAY-001|display|Unit-valued factor-system relation|NOE-P41-KO-U11-PROOF-002|2|132|134|U11:13:15|equation_for:NOE-P41-KO-U11-PROOF-002
NOE-P41-KO-U11-PARA-002|paragraph|Substitution of the cyclic generator|NOE-P41-KO-U11-PROOF-002|3|135|135|U11:16:16|
NOE-P41-KO-U11-DISPLAY-002|display|Formula for powers of the cyclic generator|NOE-P41-KO-U11-PROOF-002|4|136|138|U11:17:19|equation_for:NOE-P41-KO-U11-PROOF-002
NOE-P41-KO-U11-PARA-003|paragraph|Transition to group order f|NOE-P41-KO-U11-PROOF-002|5|139|139|U11:20:20|
NOE-P41-KO-U11-DISPLAY-003|display|Formula for alpha as a product of units|NOE-P41-KO-U11-PROOF-002|6|140|142|U11:21:23|equation_for:NOE-P41-KO-U11-PROOF-002
NOE-P41-KO-U11-PARA-004|paragraph|Splitting conclusion and converse|NOE-P41-KO-U11-PROOF-002|7|143|143|U11:24:24|
NOE-P41-KO-U12-PROOF-001|proof|Final proof of the principal genus theorem|NOE-P41-KO-U08-THEOREM-001|1|145|145|U12:12:12|proves:NOE-P41-KO-U08-THEOREM-001,cross_reference:NOE-P41-KO-U09-LEMMA-001,cross_reference:NOE-P41-KO-U09-LEMMA-002
NOE-P41-KO-U12-PARA-001|paragraph|Combination of the two auxiliary lemmas|NOE-P41-KO-U12-PROOF-001|1|145|145|U12:12:12|
NOE-P41-KO-U12-PARA-002|paragraph|Cyclic specialization through norm residues|NOE-P41-KO-U12|2|147|147|U12:14:14|
NOE-P41-KO-U12-RECEIPT-001|receipt|Journal receipt date|NOE-P41-KO-U12|3|149|151|U12:16:18|
'@

$allowedTypes = [System.Collections.Generic.HashSet[string]]::new([string[]]@(
    'work', 'unit', 'title', 'author', 'publication_note', 'section_heading',
    'subsection_heading', 'division_heading', 'paragraph', 'footnote',
    'bibliography_item', 'display', 'definition', 'theorem', 'formulation',
    'lemma', 'proof', 'proof_step', 'remark', 'transition', 'receipt'
))
$allowedRelations = [System.Collections.Generic.HashSet[string]]::new([string[]]@(
    'contains', 'embedded_in', 'continues', 'cross_reference', 'cites',
    'proves', 'statement_of', 'equation_for', 'note_for', 'bibliography_for'
))

$sourceFileHash = Get-FileSha256 $sourcePath
$targetFileHash = [ordered]@{}
foreach ($unit in $targets.Keys) {
    if (-not (Test-Path -LiteralPath $targets[$unit])) {
        throw "Missing target file for ${unit}: $($targets[$unit])"
    }
    $targetFileHash[$unit] = Get-FileSha256 $targets[$unit]
}

$specs = [System.Collections.Generic.List[object]]::new()
$manifestLines = $manifestText.Split([char]10, [System.StringSplitOptions]::RemoveEmptyEntries)
foreach ($rawLine in $manifestLines) {
    $line = $rawLine.TrimEnd([char]13)
    if ([string]::IsNullOrWhiteSpace($line)) {
        continue
    }
    $parts = $line.Split([char]'|')
    if ($parts.Count -ne 9) {
        throw "Manifest row does not have 9 columns: $line"
    }
    $targetSpecs = @($parts[7].Split([char]',', [System.StringSplitOptions]::RemoveEmptyEntries) | ForEach-Object { Convert-TargetSpec $_ })
    $relationSpecs = @($parts[8].Split([char]',', [System.StringSplitOptions]::RemoveEmptyEntries) | ForEach-Object { Convert-RelationSpec $_ })
    $specs.Add([pscustomobject]@{
        id = $parts[0]
        type = $parts[1]
        label = $parts[2]
        parent = if ([string]::IsNullOrEmpty($parts[3])) { $null } else { $parts[3] }
        order = [int]$parts[4]
        source_start = [int]$parts[5]
        source_end = [int]$parts[6]
        target_specs = $targetSpecs
        relation_specs = $relationSpecs
    })
}

$records = foreach ($spec in $specs) {
    $relations = [System.Collections.Generic.List[object]]::new()
    if ($null -ne $spec.parent) {
        $relations.Add([ordered]@{ relation = 'embedded_in'; target_id = $spec.parent })
    }
    foreach ($relationSpec in $spec.relation_specs) {
        $relations.Add([ordered]@{ relation = $relationSpec.relation; target_id = $relationSpec.target_id })
    }
    $targetLocators = foreach ($targetSpec in $spec.target_specs) {
        $targetPath = $targets[$targetSpec.unit]
        [ordered]@{
            unit_id = $targetSpec.unit
            path = $targetPath
            line_start = $targetSpec.line_start
            line_end = $targetSpec.line_end
            file_sha256 = $targetFileHash[$targetSpec.unit]
            slice_sha256_lf = Get-LfSliceSha256 $targetPath $targetSpec.line_start $targetSpec.line_end
        }
    }
    $cursorUnit = $spec.target_specs[-1].unit
    $baseRecord = [ordered]@{
        schema_version = '1.1'
        record_id = $spec.id
        work_id = 'NOE-P41'
        structure_type = $spec.type
        label = $spec.label
        parent_id = $spec.parent
        order = $spec.order
        source_language = 'de'
        target_language = 'ko-KR'
        authority_state = 'preserved_interval_historical_binding_pointer_pending'
        source_locator = [ordered]@{
            path = $sourcePath
            line_start = $spec.source_start
            line_end = $spec.source_end
            file_sha256 = $sourceFileHash
            slice_sha256_lf = Get-LfSliceSha256 $sourcePath $spec.source_start $spec.source_end
        }
        target_locators = @($targetLocators)
        relations = @($relations)
        completion_state = 'producer_draft_text_covered'
        review_state = 'unchecked'
        publication_state = 'private_not_for_publication'
        continuation_cursor = $unitCursor[$cursorUnit]
    }
    $canonical = $baseRecord | ConvertTo-Json -Compress -Depth 12
    $baseRecord.record_sha256 = Get-TextSha256 $canonical
    [pscustomobject]$baseRecord
}

$errors = [System.Collections.Generic.List[string]]::new()
if ($sourceFileHash -ne $expectedSourceFileHash) {
    $errors.Add("source file hash mismatch: expected $expectedSourceFileHash got $sourceFileHash")
}
foreach ($unit in $unitSourceLines.Keys) {
    $range = $unitSourceLines[$unit]
    $actual = Get-LfSliceSha256 $sourcePath $range[0] $range[1]
    if ($actual -ne $expectedUnitSourceHash[$unit]) {
        $errors.Add("source unit hash mismatch for ${unit}: expected $($expectedUnitSourceHash[$unit]) got $actual")
    }
}

$ids = @($records.record_id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) {
    $errors.Add('duplicate record_id')
}
$idSet = [System.Collections.Generic.HashSet[string]]::new([string[]]$ids)
foreach ($record in $records) {
    if ($record.record_id -notmatch '^NOE-P41-KO-[A-Z0-9-]+$') {
        $errors.Add("invalid record_id $($record.record_id)")
    }
    if (-not $allowedTypes.Contains($record.structure_type)) {
        $errors.Add("invalid structure type $($record.structure_type) for $($record.record_id)")
    }
    if ($record.parent_id -and -not $idSet.Contains($record.parent_id)) {
        $errors.Add("missing parent $($record.parent_id) for $($record.record_id)")
    }
    if ($record.source_locator.file_sha256 -ne (Get-FileSha256 $record.source_locator.path)) {
        $errors.Add("source file hash mismatch for $($record.record_id)")
    }
    $sourceSlice = Get-LfSliceSha256 $record.source_locator.path $record.source_locator.line_start $record.source_locator.line_end
    if ($sourceSlice -ne $record.source_locator.slice_sha256_lf) {
        $errors.Add("source slice hash mismatch for $($record.record_id)")
    }
    if ($record.target_locators.Count -lt 1) {
        $errors.Add("missing target locator for $($record.record_id)")
    }
    foreach ($locator in $record.target_locators) {
        if ($locator.file_sha256 -ne (Get-FileSha256 $locator.path)) {
            $errors.Add("target file hash mismatch for $($record.record_id) / $($locator.unit_id)")
        }
        $targetSlice = Get-LfSliceSha256 $locator.path $locator.line_start $locator.line_end
        if ($targetSlice -ne $locator.slice_sha256_lf) {
            $errors.Add("target slice hash mismatch for $($record.record_id) / $($locator.unit_id)")
        }
    }
    foreach ($relation in $record.relations) {
        if (-not $allowedRelations.Contains($relation.relation)) {
            $errors.Add("invalid relation $($relation.relation) for $($record.record_id)")
        }
        if (-not $idSet.Contains($relation.target_id)) {
            $errors.Add("missing relation target $($relation.target_id) for $($record.record_id)")
        }
    }
    if ($record.completion_state -ne 'producer_draft_text_covered' -or
        $record.review_state -ne 'unchecked' -or
        $record.publication_state -ne 'private_not_for_publication') {
        $errors.Add("state violation for $($record.record_id)")
    }
}

$requiredStructureTypes = @(
    'work', 'unit', 'title', 'author', 'publication_note', 'section_heading',
    'subsection_heading', 'division_heading', 'paragraph', 'footnote',
    'bibliography_item', 'display', 'definition', 'theorem', 'formulation',
    'lemma', 'proof', 'proof_step', 'remark', 'transition', 'receipt'
)
foreach ($requiredType in $requiredStructureTypes) {
    if (-not ($records.structure_type -contains $requiredType)) {
        $errors.Add("required touched structure type absent: $requiredType")
    }
}

$jsonlPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.jsonl'
$csvPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX.csv'
$reportPath = Join-Path $indexDir 'PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json'
$jsonLines = @($records | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 12 })
[System.IO.File]::WriteAllLines($jsonlPath, $jsonLines, $utf8NoBom)

$csvRows = $records | ForEach-Object {
    [pscustomobject]@{
        record_id = $_.record_id
        work_id = $_.work_id
        structure_type = $_.structure_type
        label = $_.label
        parent_id = $_.parent_id
        order = $_.order
        source_path = $_.source_locator.path
        source_line_start = $_.source_locator.line_start
        source_line_end = $_.source_locator.line_end
        source_file_sha256 = $_.source_locator.file_sha256
        source_slice_sha256_lf = $_.source_locator.slice_sha256_lf
        target_units = (($_.target_locators | ForEach-Object { $_.unit_id }) -join ';')
        target_locators_json = ($_.target_locators | ConvertTo-Json -Compress -Depth 6)
        relations_json = ($_.relations | ConvertTo-Json -Compress -Depth 6)
        source_language = $_.source_language
        target_language = $_.target_language
        authority_state = $_.authority_state
        completion_state = $_.completion_state
        review_state = $_.review_state
        publication_state = $_.publication_state
        continuation_cursor = $_.continuation_cursor
        record_sha256 = $_.record_sha256
    }
}
$csvRows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8

$writtenLines = [System.IO.File]::ReadAllLines($jsonlPath, $utf8NoBom)
if ($writtenLines.Count -ne $records.Count) {
    $errors.Add("JSONL row count mismatch: expected $($records.Count) got $($writtenLines.Count)")
}
foreach ($writtenLine in $writtenLines) {
    $parsed = $writtenLine | ConvertFrom-Json -Depth 20
    $baseLine = $writtenLine -replace ',"record_sha256":"[A-F0-9]{64}"}$', '}'
    $replayedHash = Get-TextSha256 $baseLine
    if ($replayedHash -ne $parsed.record_sha256) {
        $errors.Add("record self-hash mismatch for $($parsed.record_id)")
    }
}
$csvReplay = @(Import-Csv -LiteralPath $csvPath)
if ($csvReplay.Count -ne $records.Count) {
    $errors.Add("CSV row count mismatch: expected $($records.Count) got $($csvReplay.Count)")
}
if (($csvReplay.record_id | Sort-Object -Unique).Count -ne $csvReplay.Count) {
    $errors.Add('CSV duplicate record_id')
}

$typeCounts = [ordered]@{}
foreach ($group in ($records | Group-Object structure_type | Sort-Object Name)) {
    $typeCounts[$group.Name] = $group.Count
}
$report = [ordered]@{
    schema = 'PRODUCER_STRUCTURAL_INDEX.schema.json'
    builder = 'build_and_validate_structural_index.ps1'
    status = if ($errors.Count -eq 0) { 'pass' } else { 'fail' }
    record_count = $records.Count
    unique_record_count = ($ids | Sort-Object -Unique).Count
    latest_record_id = $records[-1].record_id
    type_counts = $typeCounts
    source_file_sha256 = $sourceFileHash
    source_unit_hashes_verified = $expectedUnitSourceHash
    target_file_sha256 = $targetFileHash
    jsonl_sha256 = Get-FileSha256 $jsonlPath
    csv_sha256 = Get-FileSha256 $csvPath
    errors = @($errors)
    continuation_cursor = $unitCursor.U12
    scope_note = 'Mechanical producer structure metadata only. Pairing and type labels are producer editorial inference; no source, Korean, formula, completeness, compile, render, checker, certification, or publication validation.'
}
[System.IO.File]::WriteAllText($reportPath, ($report | ConvertTo-Json -Depth 12), $utf8NoBom)
if ($errors.Count -gt 0) {
    throw "Structural index validation failed: $($errors -join '; ')"
}
Write-Output ($report | ConvertTo-Json -Compress -Depth 12)
