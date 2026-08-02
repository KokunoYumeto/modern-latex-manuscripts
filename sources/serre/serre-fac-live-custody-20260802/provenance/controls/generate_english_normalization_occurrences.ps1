param(
    [string]$OutputPath = (Join-Path $PSScriptRoot 'ENGLISH_NORMALIZATION_OCCURRENCES.csv')
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$progressPath = Join-Path $PSScriptRoot 'TRANSLATION_PROGRESS.csv'
$progress = Import-Csv -LiteralPath $progressPath

$policies = @(
    [pscustomobject]@{ id='FAC-EN-N0001'; regex='(?i)\bcoherent shea(?:f|ves)\b'; source='faisceau(x) coherent(s)'; class='terminology'; rationale='standard modern English algebraic-geometry term' },
    [pscustomobject]@{ id='FAC-EN-N0002'; regex='(?i)\bcoverings?\b|\bfiner\b'; source='recouvrement(s); plus fin'; class='terminology'; rationale='standard Cech-cohomology register and source preorder direction' },
    [pscustomobject]@{ id='FAC-EN-N0003'; regex='(?i)\bdirected(?:\s+(?:preorder|ordered set|relation))?\b'; source='filtrant(e); ordonne filtrant'; class='terminology'; rationale='standard English order/direct-limit terminology' },
    [pscustomobject]@{ id='FAC-EN-N0004'; regex='(?i)\bdirect limits?\b'; source='limite(s) inductive(s)'; class='terminology'; rationale='standard English categorical terminology' },
    [pscustomobject]@{ id='FAC-EN-N0005'; regex='(?i)\bcoboundar(?:y|ies)\b'; source='cobord(s)'; class='terminology'; rationale='preserves cohomological rather than homological variance' },
    [pscustomobject]@{ id='FAC-EN-N0006'; regex='\\mathcal\{[A-Z]\}'; source='\\mathfrak{A-Z}'; class='typographic_normalization'; rationale='consistent established English workpass typography; all indices and operations retained' },
    [pscustomobject]@{ id='FAC-EN-N0007'; regex='\\geq(?!q)'; source='\\geqq'; class='typographic_normalization'; rationale='portable modern TeX inequality glyph with unchanged relation' },
    [pscustomobject]@{ id='FAC-EN-N0008'; regex='\\mapsto'; source='\\to in prose element assignment'; class='semantic_typography'; rationale='distinguishes element assignment from a morphism arrow' },
    [pscustomobject]@{ id='FAC-EN-N0010'; regex='\\footnote\{'; source='physical bottom-page footnote text'; class='layout_restoration'; rationale='attaches translated note at its logical source marker' },
    [pscustomobject]@{ id='FAC-EN-N0013'; regex='(?i)\b(?:non-)?Hausdorff(?:ness)?\b'; source='separe; non separe'; class='terminology'; rationale='standard English topological terminology; preserves the source separation property' },
    [pscustomobject]@{ id='FAC-EN-N0014'; regex='(?i)\bprealgebraic variet(?:y|ies)\b'; source='variete(s) prealgebrique(s)'; class='historical_terminology'; rationale='preserves Serre historical intermediate category and does not modernize it into schemes' },
    [pscustomobject]@{ id='FAC-EN-N0015'; regex='(?i)\bbiregular isomorphisms?\b'; source='isomorphisme(s) biregulier(s)'; class='terminology'; rationale='standard algebraic-geometry term retaining both regularity directions' },
    [pscustomobject]@{ id='FAC-EN-N0016'; regex='(?i)\bregular maps?\b'; source='application(s) reguliere(s)'; class='terminology'; rationale='standard English morphism terminology in the source-defined category' },
    [pscustomobject]@{ id='FAC-EN-N0017'; regex='(?i)\blocally closed\b'; source='localement ferme(e)(s)'; class='terminology'; rationale='standard topological and algebraic-geometry term' },
    [pscustomobject]@{ id='FAC-EN-N0018'; regex='(?i)\bsheaf of local rings\b'; source='faisceau des anneaux locaux'; class='terminology'; rationale='standard English name for Serre local-ring sheaf' },
    [pscustomobject]@{ id='FAC-EN-N0019'; regex='(?i)\bproduct variet(?:y|ies)\b'; source='variete(s) produit'; class='terminology'; rationale='standard English categorical product terminology' },
    [pscustomobject]@{ id='FAC-EN-N0020'; regex='(?i)\bsubvariet(?:y|ies)\b'; source='sous-variete(s)'; class='terminology'; rationale='preserves Serre stated broad usage and accompanying Weil caveat' },
    [pscustomobject]@{ id='FAC-EN-N0021'; regex='(?i)\bZariski topology\b'; source='topologie de Zariski'; class='terminology'; rationale='standard proper-name terminology' },
    [pscustomobject]@{ id='FAC-EN-N0022'; regex='(?i)\bcharts?\b'; source='carte(s)'; class='terminology'; rationale='standard local-coordinate terminology for algebraic varieties' },
    [pscustomobject]@{ id='FAC-EN-N0023'; regex='(?i)\bseparation condition\b'; source='condition de separation'; class='historical_terminology'; rationale='preserves Serre explicit analogy rather than silently replacing the phrase by Hausdorff axiom' },
    [pscustomobject]@{ id='FAC-EN-N0024'; regex='\(\\varphi_i\\times\\varphi_j\)\(X_\{ij\}\)'; source='\\varphi_i \\times \\varphi_j(X_{ij})'; class='semantic_typography'; rationale='parentheses make application of the product map explicit without altering the authorial definition' },
    [pscustomobject]@{ id='FAC-EN-N0025'; regex='(?i)\balgebraic fiber space\b'; source='espace fibre algebrique'; class='historical_terminology'; rationale='established English phrase for the cited Weil-era construction' },
    [pscustomobject]@{ id='FAC-EN-N0026'; regex='(?i)\bfield of rational functions\b'; source='corps des fonctions rationnelles'; class='terminology'; rationale='standard English algebraic-geometry term while retaining Serre word order' },
    [pscustomobject]@{ id='FAC-EN-N0027'; regex='(?i)\blocally constant\b'; source='localement constant'; class='terminology'; rationale='standard sheaf-theoretic terminology' },
    [pscustomobject]@{ id='FAC-EN-N0028'; regex='(?i)\bsheaf of fields\b'; source='faisceau de corps'; class='terminology'; rationale='standard English name for a sheaf whose stalks and local rings are fields' },
    [pscustomobject]@{ id='FAC-EN-N0029'; regex='(?i)\bintegral domains?\b'; source='anneau(x) d''integrite'; class='terminology'; rationale='standard English commutative-algebra term' },
    [pscustomobject]@{ id='FAC-EN-N0030'; regex='(?i)\bfields? of fractions\b'; source='corps des fractions; corps des quotients'; class='terminology'; rationale='standard English term for the fraction field of an integral domain' },
    [pscustomobject]@{ id='FAC-EN-N0031'; regex='(?i)\btranscendence degree\b'; source='degre de transcendance'; class='terminology'; rationale='standard English field-theory term' },
    [pscustomobject]@{ id='FAC-EN-N0032'; regex='(?i)\bspecialization ring\b'; source='anneau de specialisation'; class='historical_terminology'; rationale='retains Serre and Weil historical term rather than silently replacing it by valuation ring' },
    [pscustomobject]@{ id='FAC-EN-N0033'; regex='\\sup_i'; source='\\mathrm{Sup} \\dim Y_i'; class='semantic_typography'; rationale='binds the already visible index i to the supremum operator without changing the dimension definition' },
    [pscustomobject]@{ id='FAC-EN-N0034'; regex='(?i)\balgebraic shea(?:f|ves)\b'; source='faisceau(x) algebrique(s)'; class='terminology'; rationale='standard direct English term for an O_V-module sheaf in Serre sense' },
    [pscustomobject]@{ id='FAC-EN-N0035'; regex='(?i)\balgebraic homomorphisms?\b'; source='homomorphisme(s) algebrique(s)'; class='terminology'; rationale='retains the source category and distinguishes O_V-linearity' },
    [pscustomobject]@{ id='FAC-EN-N0036'; regex='(?i)\bcokernels?\b'; source='conoyau(x)'; class='terminology'; rationale='standard English categorical term' },
    [pscustomobject]@{ id='FAC-EN-N0037'; regex='(?i)\bshea(?:f|ves) of finite type\b'; source='faisceau(x) de type fini'; class='terminology'; rationale='source-transparent English finiteness terminology without strengthening to finite presentation' },
    [pscustomobject]@{ id='FAC-EN-N0038'; regex='\bNoetherian\b'; source='noetherien'; class='terminology'; rationale='standard capitalization of the proper-name adjective in English' },
    [pscustomobject]@{ id='FAC-EN-N0039'; regex='(?i)\bideal shea(?:f|ves)\b'; source='faisceau(x) d''ideaux'; class='terminology'; rationale='standard English name for the subsheaf of ideals defined by a closed subvariety' },
    [pscustomobject]@{ id='FAC-EN-N0040'; regex='(?i)\bannihilators?\b'; source='annulateur(s)'; class='terminology'; rationale='standard module-theoretic term for the ideal acting by zero' },
    [pscustomobject]@{ id='FAC-EN-N0041'; regex='(?i)\bextend(?:ed|ing)? [^.;]*? by zero\b'; source='prolonger par 0'; class='terminology'; rationale='standard sheaf-theoretic phrase for the source construction' },
    [pscustomobject]@{ id='FAC-EN-N0042'; regex='(?i)\bshea(?:f|ves) of fractional ideals\b'; source='faisceau(x) d''ideaux fractionnaires'; class='terminology'; rationale='standard fractional-ideal terminology while preserving Serre''s sheaf-level formulation' },
    [pscustomobject]@{ id='FAC-EN-N0043'; regex='(?i)\bstructure group\b'; source='groupe structural'; class='terminology'; rationale='standard English bundle terminology without changing the group or its action' },
    [pscustomobject]@{ id='FAC-EN-N0044'; regex='(?i)\bsheaf of germs of sections\b'; source='faisceau des germes de sections'; class='terminology'; rationale='direct standard English rendering that preserves the germ-level construction' },
    [pscustomobject]@{ id='FAC-EN-N0045'; regex='(?i)\bnonsingular\b'; source='sans singularites'; class='historical_terminology'; rationale='standard English variety terminology in the article''s pre-scheme register' },
    [pscustomobject]@{ id='FAC-EN-N0046'; regex='(?i)\baffine open subsets?\b'; source='ouvert(s) affine(s)'; class='terminology'; rationale='standard English ordering for an open subset that is affine' },
    [pscustomobject]@{ id='FAC-EN-N0047'; regex='(?i)\bvanish(?:es|ing)? on\b'; source='nul(s) sur'; class='terminology'; rationale='standard polynomial-function terminology and faithful to the zero-locus condition' },
    [pscustomobject]@{ id='FAC-EN-N0048'; regex='\\Delta\\cap\(U\\times V\)'; source='\\Delta\\cap U\\times V'; class='semantic_typography'; rationale='parentheses make the only type-correct intersection explicit without changing the subset' },
    [pscustomobject]@{ id='FAC-EN-N0049'; regex='(?i)\bHilbert''s Nullstellensatz\b'; source='theoreme des zeros de Hilbert'; class='terminology'; rationale='standard English proper name for the cited theorem' },
    [pscustomobject]@{ id='FAC-EN-N0050'; regex='(?i)\bclearing denominators\b'; source='en chassant les denominateurs'; class='terminology'; rationale='standard algebraic phrase for multiplying through by a common denominator' }
)

function Get-StableId([string]$value) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($value)
        $hash = $sha.ComputeHash($bytes)
        $hex = -join ($hash | ForEach-Object { $_.ToString('x2') })
        return 'FAC-EN-NOCC-' + $hex.Substring(0,16).ToUpperInvariant()
    }
    finally {
        $sha.Dispose()
    }
}

$rows = [System.Collections.Generic.List[object]]::new()
foreach ($unit in $progress) {
    $targetRel = $unit.target_tex
    $targetAbs = Join-Path $root ($targetRel -replace '/', '\')
    if (-not (Test-Path -LiteralPath $targetAbs)) {
        throw "Missing target component for normalization replay: $targetRel"
    }
    $lines = Get-Content -LiteralPath $targetAbs
    for ($lineIndex = 0; $lineIndex -lt $lines.Count; $lineIndex++) {
        $line = $lines[$lineIndex]
        foreach ($policy in $policies) {
            foreach ($match in [regex]::Matches($line, $policy.regex)) {
                $lineNumber = $lineIndex + 1
                $column = $match.Index + 1
                $identity = '{0}|{1}|{2}|{3}|{4}' -f $policy.id,$targetRel,$lineNumber,$column,$match.Value
                $rows.Add([pscustomobject][ordered]@{
                    occurrence_id = Get-StableId $identity
                    policy_id = $policy.id
                    unit_id = $unit.unit_id
                    source_tex = $unit.source_tex
                    source_start_line = $unit.source_start_line
                    source_end_line = $unit.source_end_line
                    printed_start = $unit.printed_start
                    printed_end = $unit.printed_end
                    target_file = $targetRel
                    target_line = $lineNumber
                    target_column = $column
                    source_form = $policy.source
                    selected_form = $match.Value
                    decision_class = $policy.class
                    rationale = $policy.rationale
                    status = 'active_occurrence'
                })
            }
        }
    }
}

$ordered = $rows | Sort-Object target_file,@{Expression={[int]$_.target_line}},@{Expression={[int]$_.target_column}},policy_id
$ordered | Export-Csv -LiteralPath $OutputPath -NoTypeInformation -Encoding utf8

$ids = @($ordered.occurrence_id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) {
    throw 'Normalization occurrence IDs are not unique.'
}

[pscustomobject]@{
    output = $OutputPath
    rows = $ordered.Count
    unique_ids = $true
}
