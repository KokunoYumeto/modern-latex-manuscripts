$ErrorActionPreference = 'Stop'
$ledgerPath = Join-Path $PSScriptRoot 'difficulty_ledger.jsonl'
$csvPath = Join-Path $PSScriptRoot 'difficulty_ledger.csv'
if (Test-Path -LiteralPath $ledgerPath) { throw "Append-only ledger already exists: $ledgerPath" }
if (Test-Path -LiteralPath $csvPath) { throw "CSV projection already exists: $csvPath" }

$sourcePath = '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/03_working_translations/noether_paper41_zh_translation_001_20260722/source/Noether_Paper41_CurrentGermanAuthority_interval.tex'
$snapshotHash = 'C265058425E5E2D1A2289CC03A9DDEDDDF4803A3215DC3F173B93E7AB69D60ED'
$historicalHash = '443EF950D7D45DC6D9E44A9B87501620C10DA873E50E5F2B253ECCAE6A946D27'
$root = '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/03_working_translations/noether_paper41_ko_translation_001_20260804'
$unitHashes = [ordered]@{
  U01='BAD33EF459284C4E06A877CEBD624F8C843DED51B82A608475F7FB9726F0228C'; U02='8C0BC86950AD752B9CAED52C54765F6AF6E3592D48996200313845B44942F6BD'
  U03='E1509DFE9ED80F79ED65F770EABF148C56CB853B2E7BD075E629175E2D426EFD'; U04='F0D1FF2818BD95257249E93DB56E891343DF2EB025DD3F46987461ACCA05A0FC'
  U05='BCEA8450C5DC412DA1506DD0A8A935AD5517D2B03637C57698B6C3D504FB7788'; U06='1EC47AC260130703D0C0313186283365D339F04472184000D219ED44962EA55D'
  U07='6B1BAB1A613156C833C091DFE9C98D8C63610545811F24A5E27EF65FE9751A15'; U08='1432D5DDE7E39212CE1D1EC7478348C0856AEB80A6D4FB7324954781A3075BF5'
  U09='78A0D977D2F04C537D3DFD91AA23ED2F221EBDA5D5A4A8F8081EA0CFCB93520F'; U10='D31F076B49A420DB830B465D325C4360EA283D3B6A23CE67E2416AC225FAEC24'
  U11='6F8C5A72030ED3C658C0C0CA0D99077E88F9C4B967BEA672D1F3CE148DE1C2F9'; U12='D0259D62D1D60476EE3F16E2E22BDFB8CDAD7A4978DC12683A5C0999AEA4DDBE'
}
$targetHashes = [ordered]@{
  U01='AA6C1E40F4CAC15106AD2451B9B97EF071A684C6C555FD78475633A58E5597C0'; U02='B717990BFB495620551659CBCFEBF58620BD912A710518C448E462CEC2D94C6E'
  U03='5DEF83537B9FC66310CD0DCE291F8E12F40ABD127A0FB2C2AA3A2AD9AE6D57DF'; U04='16D83FC0EE14E8CE45B530946A0F490A04B36985303A6670868EBC31822779CD'
  U05='4CDA25B27F69215AC6AC2ABE437A087419960FF39F0955F254394EA0A01AE0B0'; U06='DEB580BB167B165B3DE40777A9F18B9E6D356FBE3CB2E552BB202E374E99A164'
  U07='458C2DEF857180D29A71BE9E977498EA50C8688CB0297CA87E79AE0CE2EF505A'; U08='D231193F8933E00701296564D113A677A505FCE761FF1F0DDC2EAB0B07D90D12'
  U09='0051DCA8B4FF39B374FBE61D88BBF39F0E99A9A767B28073B2212A967C4DA00A'; U10='B3A79835C998F7C056C6C7721C432EEE4DE6ED5D54B652FC242B7C3C814EC7A0'
  U11='A0DD197BA74A1C065B18652C1C8EA830E56461C5C23A73E1020011ECA9E1FE84'; U12='33E5D1EBE1620A9AD2E3E4E22EB6E3689D0CBDC238010306CF62083A8DA517E3'
}

function New-Authority([string[]]$units, [string[]]$locators) {
  $slices = [ordered]@{}
  foreach ($u in $units) { if ($unitHashes.Contains($u)) { $slices[$u] = $unitHashes[$u] } }
  [ordered]@{ path=$sourcePath; snapshot_sha256=$snapshotHash; historical_whole_source_sha256=$historicalHash; locators=$locators; unit_slice_sha256=$slices }
}
function New-Target([string]$id, [string]$path, $hash, [string]$state='frozen_producer_identity') {
  [ordered]@{ artifact_id=$id; path=$path; sha256=$hash; hash_state=$state }
}
function New-Cause([string]$kind,[string]$detail,$path=$null,$hash=$null) { [ordered]@{kind=$kind;detail=$detail;path=$path;sha256=$hash} }
function New-Evidence([string]$kind,[string]$detail,$path=$null,$hash=$null) { [ordered]@{kind=$kind;detail=$detail;path=$path;sha256=$hash} }
function New-Attempt([string]$approach,[string]$outcome,[string]$status) { [ordered]@{approach=$approach;outcome=$outcome;status=$status} }

$records = [System.Collections.Generic.List[object]]::new()
$script:previous = $null
function Add-Record {
  param([string[]]$Units,[hashtable]$Authority,[object[]]$Targets,[string]$Category,[string]$Sense,[string[]]$Facts,[string]$Symptom,[object[]]$Causes,[object[]]$Attempts,[string[]]$Rejected,[string]$State,[string]$Resolution,[object[]]$Evidence,[string]$Risk,[string[]]$Cues,[string]$Mandarin,[string]$Basin,[string[]]$Decisions,[string[]]$Structures,[string]$Lesson,[string]$Revisit)
  $seq = $records.Count + 1
  $obj = [ordered]@{
    schema_version='1.0.0'; record_id=('CJK-KO-P41-HARD-{0:D3}' -f $seq); recorded_at='2026-08-04'; time_precision='day'; append_sequence=$seq
    previous_record_sha256=$script:previous; work_id='NOE-P41-KO'; unit_ids=$Units; authority=$Authority; targets=$Targets; category=$Category; sense_window=$Sense
    fact_classes=$Facts; symptom=$Symptom; cause_evidence=$Causes; attempted_approaches=$Attempts; rejected_approaches=$Rejected
    resolution_state=$State; resolution=$Resolution; evidence=$Evidence; residual_risk=$Risk; recurrence_cues=$Cues
    mandarin_simplified_dominance_risk=$Mandarin; lexical_attractor_basin=$Basin; related_decision_ids=$Decisions; related_structural_ids=$Structures
    transferable_lesson=$Lesson; review_state='producer_metadata_unchecked'; supersession_state='current'; revisit_condition=$Revisit; record_sha256=$null
  }
  $placeholder = $obj | ConvertTo-Json -Compress -Depth 20
  $hash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($placeholder)))
  $suffix = '"record_sha256":null}'
  if (-not $placeholder.EndsWith($suffix)) { throw "record_sha256 is not final for sequence $seq" }
  $line = $placeholder.Substring(0,$placeholder.Length-$suffix.Length) + '"record_sha256":"' + $hash + '"}'
  $records.Add([pscustomobject]@{ Object=$obj; Line=$line; Hash=$hash })
  $script:previous = $hash
}

$allUnits=@('U01','U02','U03','U04','U05','U06','U07','U08','U09','U10','U11','U12')
Add-Record $allUnits (New-Authority $allUnits @('snapshot local lines 1-154','producer body 1-151','controls 153-154 excluded')) @(
  (New-Target 'CANON-BINDER' '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/noether/07_german_canon_control/receipts/KOREAN_P41_U01_U12_BINDER_20260804.json' '95D0E69B6D32FD93801C3FDC4C519FAA9AB7CA867538E1CD9E2096EFAB253A91'),
  (New-Target 'POINTER-V003' '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/noether/07_german_canon_control/pointers/NOETH_DE_AUTHORITY_POINTER_v003_20260804.json' '932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197')
) 'authority_binding' 'Stored LF snapshot versus current CRLF authority and missing historical P16 whole ancestry.' @('source_fact','computation','external_or_human_validation') 'Historical coordinate debt existed even though the preserved interval hash was exact.' @(
  (New-Cause 'source_fact' 'Historical P16 whole file and pointer path are unavailable; only the preserved interval survived.' $sourcePath $snapshotHash),
  (New-Cause 'external_or_human_validation' 'Canon owner independently rebound the complete interval by strict newline normalization.' '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/noether/07_german_canon_control/receipts/KOREAN_P41_U01_U12_BINDER_20260804.json' '95D0E69B6D32FD93801C3FDC4C519FAA9AB7CA867538E1CD9E2096EFAB253A91')
) @(
  (New-Attempt 'Treat historical P16 coordinates as current authority.' 'Rejected because the whole file is missing and non-replayable.' 'rejected'),
  (New-Attempt 'Request coordinate-only canon binder.' 'Accepted; normalized identity to ED0001 and named public layers was returned.' 'accepted')
) @('Do not infer a whole-file ancestry edge to missing P16.','Do not treat R823 Analogon/Anologon lineage delta as a translator-confirmed defect.') 'resolved' 'Pointer v003 and the immutable P41 binder close coordinate/tooling debt for this exact interval.' @(
  (New-Evidence 'canon_receipt' 'SAFE normalized-identical; no target inspected.' '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/noether/07_german_canon_control/receipts/KOREAN_P41_U01_U12_BINDER_20260804.json' '95D0E69B6D32FD93801C3FDC4C519FAA9AB7CA867538E1CD9E2096EFAB253A91')
) 'R823 retains a one-token divergent ancestor reading and original-print adjudication remains absent.' @('lost historical whole path','raw byte inequality caused solely by CRLF/LF','branch token difference without checker evidence') 'not_applicable' 'not_applicable' @('CJK-KO-P41-001','CJK-KO-P41-003','CJK-KO-P41-004') @('NOE-P41-KO-WORK-001') 'Bind a preserved unit directly to a current content-addressed authority; never let missing whole ancestry invalidate a normalized-identical unit.' 'Revisit only if a checker-confirmed primary-source finding is submitted under pointer v003.'

Add-Record $allUnits (New-Authority $allUnits @('all producer units','language evidence shelf')) @(
  (New-Target 'CHOICES' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'language_evidence_gap' 'Hangul/Hanja and South-/North-Korean standards cannot be inferred from Chinese/Japanese cognates.' @('source_fact','editorial_inference','model_preference') 'No accessible Korean-native historical algebra corpus or ko-KP evidence authorized the new lexicon.' @(
  (New-Cause 'source_fact' 'The surviving local custody shelf is Mandarin-Simplified-dominant and target-disjoint.'),
  (New-Cause 'editorial_inference' 'Cross-language cognacy creates a lexical-attractor risk but not Korean evidence.')
) @(
  (New-Attempt 'Infer Hanja and pan-Korean terms from Chinese/Japanese forms.' 'Rejected as invalid cross-language authorization.' 'rejected'),
  (New-Attempt 'Use Hangul-first ko-KR and expose all new terms.' 'Accepted provisionally.' 'accepted')
) @('Do not convert Mandarin-Simplified dominance into a readiness score.','Do not claim ko-KP equivalence.') 'held' 'Keep Hanja/ko-KP decisions open and require language-specific evidence.' @(
  (New-Evidence 'producer_choices' 'Explicit evidence debt and regional/script boundary.' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'Some fluent-looking Sino-Korean choices may be unattested or regionally marked.' @('new Sino-xenic term','temptation to infer Hanja','claim that ko-KR covers ko-KP') 'active_qualitative_control' 'mixed/contested' @('CJK-KO-P41-002') @('NOE-P41-KO-WORK-001') 'Language-specific evidence debt must remain visible even when target prose is fluent.' 'Independent Korean and ko-KP specialists must return explicit evidence.'

Add-Record @('U01','U02','U05','U06') (New-Authority @('U01','U02','U05','U06') @('lines 1-20','lines 58-78')) @(
  (New-Target 'CHOICES' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'terminology' 'Hauptgeschlechtssatz; im Minimalen; im Kleinen.' @('editorial_inference','model_preference') 'The historical scope contrast can be flattened or activated by ordinary-language meanings.' @(
  (New-Cause 'editorial_inference' 'Source footnote explicitly distinguishes im Minimalen from im Kleinen.'),
  (New-Cause 'model_preference' 'Producer uses 주종정리, 최소형, 소형 without Korean attestation.')
) @(
  (New-Attempt 'Collapse both scope labels into one generic small case.' 'Rejected because it erases the source contrast.' 'rejected'),
  (New-Attempt 'Use 주종정리 / 최소형 / 소형 provisionally.' 'Accepted for checker-visible drafting.' 'accepted')
) @('Do not treat principal genus as ordinary main type.','Do not normalize the paired scope labels independently.') 'held' 'Checker must bind the theorem name and paired labels as one terminology family.' @(
  (New-Evidence 'producer_choices' 'Sense window and alternatives.' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'A global replacement may be needed across title, formulations, and proof references.' @('Hauptgeschlechtssatz in later paper','Minimalen/Kleinen contrast','ordinary-language genus attraction') 'evidence_debt' 'modern Sino-xenic coinage/calque' @('CJK-KO-P41-002') @('NOE-P41-KO-TITLE-001','NOE-P41-KO-U05') 'Resolve historically linked terminology as a family, not token by token.' 'Independent Korean class-field-theory checker decision.'

Add-Record @('U01','U02','U03','U05','U06','U08') (New-Authority @('U01','U02','U03','U05','U06','U08') @('crossed-product definitions and formulations')) @(
  (New-Target 'CHOICES' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'terminology' 'verschränktes Produkt; verschränkte Darstellung; Faktorensystem; assoziiert; Transformationsgrößen.' @('editorial_inference','model_preference') 'Several coupled cohomological senses invite literal or mutually inconsistent translations.' @(
  (New-Cause 'editorial_inference' 'Displayed relations tie all five terms into one concept family.'),
  (New-Cause 'model_preference' 'Producer uses 교차곱, 교차표현, 인자계, 연관된, 변환량.')
) @(
  (New-Attempt 'Translate verschränkt literally as 얽힌.' 'Rejected as nontechnical attraction.' 'rejected'),
  (New-Attempt 'Use crossed-product family and log cohomological equivalence debt.' 'Accepted provisionally.' 'accepted')
) @('Do not replace assoziiert locally without checking all factor-system relations.') 'held' 'Require one checker-owned terminology map across definitions, formulas, and representation classes.' @(
  (New-Evidence 'producer_choices' 'Explicit family sense window.' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) '연관된 may be weaker than cohomological equivalence; 교차표현 may lack Korean attestation.' @('factor-system coboundary','crossed representation','assoziiert near algebra similarity') 'evidence_debt' 'modern Sino-xenic coinage/calque' @('CJK-KO-P41-002') @('NOE-P41-KO-U03','NOE-P41-KO-U05','NOE-P41-KO-U08') 'Map a coupled mathematical vocabulary family before approving any individual term.' 'Independent Korean algebra/representation-theory checker.'

Add-Record @('U01','U02','U03') (New-Authority @('U01','U02','U03') @('introduction and crossed-product algebra setup')) @(
  (New-Target 'U01' "$root/targets/Noether_P41_Korean_U01_UNCHECKED.tex" $targetHashes.U01),
  (New-Target 'U03' "$root/targets/Noether_P41_Korean_U03_UNCHECKED.tex" $targetHashes.U03)
) 'terminology' 'Maximalordnung; Linearformenmodul; einfache normale Algebra.' @('editorial_inference','model_preference') 'Historical order/module/normal-algebra vocabulary collides with modern Korean senses and prior producer choices.' @(
  (New-Cause 'model_preference' 'P41 uses 극대차수 while P42 used 극대 오더.'),
  (New-Cause 'editorial_inference' 'einfache normale Algebra likely has the central-simple sense; historical Modul is module, not modulus.')
) @(
  (New-Attempt 'Silently normalize P41 to the P42 loanword.' 'Rejected because that would be unreviewed terminology editing.' 'rejected'),
  (New-Attempt 'Expose both producer choices to a checker.' 'Accepted.' 'accepted')
) @('Do not confuse Ordnung with degree/order in invariant theory.','Do not read normal as merely normal ring.') 'held' 'P41/P42 conflict remains explicit; checker must choose corpus-wide forms.' @(
  (New-Evidence 'producer_choices' 'Cross-paper adverse evidence.' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'An approved replacement must propagate across multiple papers and structural roles.' @('Ordnung family recurs','normal algebra in premodern terminology','Modul false friend') 'evidence_debt' 'mixed/contested' @('CJK-KO-P41-002') @('NOE-P41-KO-U01','NOE-P41-KO-U02','NOE-P41-KO-U03') 'Cross-paper inconsistency is adverse evidence to surface, not permission for an unreviewed global edit.' 'Corpus-wide Korean algebra checker decision.'

Add-Record @('U07','U08','U09','U12') (New-Authority @('U07','U08','U09','U12') @('class partition and principal genus statements')) @(
  (New-Target 'CHOICES' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'terminology' 'Klasseneinteilung; Hauptklasse; Einsklasse; Hauptgeschlecht; ambig; Basiselement.' @('editorial_inference','model_preference') 'Short Korean calques can activate everyday meanings rather than ideal-class structure.' @(
  (New-Cause 'model_preference' 'Producer uses 류분할, 주류, 일류, 주종, 모호(ambig), 생성원.'),
  (New-Cause 'editorial_inference' 'ambig denotes Galois-invariant/ambiguous ideal classes; Basiselement may mean an ideal generator.')
) @(
  (New-Attempt 'Use only literal 모호 and 일류 without gloss.' 'Held because fixed-class and identity-class senses may disappear.' 'held'),
  (New-Attempt 'Retain source glosses and expose alternatives.' 'Accepted provisionally.' 'accepted')
) @('Do not let 일류 attract first-rate meaning.','Do not decide Basiselement without its ideal-generator context.') 'held' 'Checker must approve a relation-aware class-field-theory lexicon.' @(
  (New-Evidence 'producer_choices' 'Sense windows and adverse alternatives.' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'Local substitutions can break the explicit equivalence among three formulations.' @('ambig class','identity/principal class','Hauptgeschlecht vector') 'evidence_debt' 'mixed/contested' @('CJK-KO-P41-002') @('NOE-P41-KO-U07','NOE-P41-KO-U08','NOE-P41-KO-U09') 'Class terminology must preserve relations, not just surface cognates.' 'Independent Korean class-field-theory checker.'

Add-Record @('U09','U10','U11','U12') (New-Authority @('U09','U10','U11','U12') @('ideal lemma and local proof')) @(
  (New-Target 'CHOICES' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'terminology' 'Modulsumme; Zerlegungsgruppe; unverzweigter Trägheitskörper; normierte zyklische Darstellung; Normenrest.' @('editorial_inference','model_preference') 'Historical local arithmetic terms are false-friend prone and are embedded in a proof chain.' @(
  (New-Cause 'editorial_inference' 'Source itself glosses Modulsumme as greatest common divisor and derives local splitting via unramified units.'),
  (New-Cause 'model_preference' 'Producer uses 가군합, 분해군, 비분기 관성체, 정규화된 순환표현, 노름잉여.')
) @(
  (New-Attempt 'Translate Modulsumme as an abstract module direct sum.' 'Rejected because source gives the ideal gcd convention.' 'rejected'),
  (New-Attempt 'Use modern local-field calques with historical sense windows.' 'Accepted provisionally.' 'accepted')
) @('Do not normalize historical Trägheitskörper without local-field evidence.','Do not read Normenrest as a numerical remainder.') 'held' 'Checker must review the local terminology and the source convention as one proof segment.' @(
  (New-Evidence 'producer_choices' 'Local arithmetic sense windows.' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'An incorrect term may invert the local/global argument even if formulas remain unchanged.' @('Trägheitskörper in historical text','Normenrest at ramified place','Modulsumme followed by gcd gloss') 'evidence_debt' 'mixed/contested' @('CJK-KO-P41-002') @('NOE-P41-KO-U09','NOE-P41-KO-U10','NOE-P41-KO-U11','NOE-P41-KO-U12') 'Open a sense window from the construction and proof role before choosing a modern cognate.' 'Independent Korean number-theory checker.'

Add-Record @('U01','U02','U03','U04') (New-Authority @('U01','U02','U03','U04') @('target write production for U01-U04')) @(
  (New-Target 'U01' "$root/targets/Noether_P41_Korean_U01_UNCHECKED.tex" $targetHashes.U01),
  (New-Target 'U02' "$root/targets/Noether_P41_Korean_U02_UNCHECKED.tex" $targetHashes.U02),
  (New-Target 'U03' "$root/targets/Noether_P41_Korean_U03_UNCHECKED.tex" $targetHashes.U03),
  (New-Target 'U04' "$root/targets/Noether_P41_Korean_U04_UNCHECKED.tex" $targetHashes.U04)
) 'producer_write_failure' 'TeX inline-math delimiters in target serialization.' @('source_fact','computation') 'A normal JavaScript string consumed backslashes before inline math delimiters in the first U01-U04 patch payload.' @(
  (New-Cause 'source_fact' 'Worker reported the escaping failure and repaired it before the frozen hashes.'),
  (New-Cause 'computation' 'Failed pre-repair hashes are unavailable because hashing occurred only after repair.')
) @(
  (New-Attempt 'Write TeX through an unescaped normal JavaScript string.' 'Failed; inline delimiters were stripped.' 'failed'),
  (New-Attempt 'Restore delimiters with apply_patch before freezing identities.' 'Accepted; Korean wording unchanged.' 'accepted')
) @('Never invent unavailable failed hashes.','Do not call delimiter restoration formula review.') 'resolved' 'Final U01-U04 hashes freeze repaired producer bytes; failure remains append-only.' @(
  (New-Evidence 'decision_log' 'Failure and final identities.' '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/00_lane_control/CJK_DECISION_LOGBOOK_20260718.md' $null)
) 'Other TeX escapes could fail if future patch payloads repeat the same string path.' @('normal JavaScript string contains TeX','backslash count unexpectedly low','inline math appears as plain parentheses') 'not_applicable' 'not_applicable' @('CJK-KO-P41-002') @('NOE-P41-KO-U01','NOE-P41-KO-U02','NOE-P41-KO-U03','NOE-P41-KO-U04') 'Protect TeX escapes at serialization time and preserve failures even when repair precedes hashing.' 'Recur if any producer target is written through a normal unescaped JavaScript string.'

Add-Record @('U05','U06','U07','U08') (New-Authority @('U05','U06','U07','U08') @('target write production for U05-U08')) @(
  (New-Target 'U05-FIRST' "$root/targets/Noether_P41_Korean_U05_UNCHECKED.tex" '4B8BA56E3DCA4B5DE4A22246CCE452CD28C5D3C2C8DEEECFA5CEE9360B9684CB' 'superseded_damaged_identity'),
  (New-Target 'U05-FINAL' "$root/targets/Noether_P41_Korean_U05_UNCHECKED.tex" $targetHashes.U05),
  (New-Target 'U06-FIRST' "$root/targets/Noether_P41_Korean_U06_UNCHECKED.tex" '66D65E137EFDFEA3ABAB4FECFD14712AE5D61726CD10ECF388C58231E643551E' 'superseded_damaged_identity'),
  (New-Target 'U06-FINAL' "$root/targets/Noether_P41_Korean_U06_UNCHECKED.tex" $targetHashes.U06),
  (New-Target 'U07-FIRST' "$root/targets/Noether_P41_Korean_U07_UNCHECKED.tex" 'A75012D4DBB2B6170E370FC89C5EEBFA6CAA91360759A3D931156C287507C698' 'superseded_damaged_identity'),
  (New-Target 'U07-FINAL' "$root/targets/Noether_P41_Korean_U07_UNCHECKED.tex" $targetHashes.U07),
  (New-Target 'U08-FIRST' "$root/targets/Noether_P41_Korean_U08_UNCHECKED.tex" 'FD0D95AB028004AA85933E0627D9F7F106BC179E8706AB216513BD5ABF89CC89' 'superseded_damaged_identity'),
  (New-Target 'U08-FINAL' "$root/targets/Noether_P41_Korean_U08_UNCHECKED.tex" $targetHashes.U08)
) 'producer_write_failure' 'TeX inline-math delimiter loss with frozen before/after identities.' @('source_fact','computation') 'First-return U05-U08 files lost backslashes before many inline delimiters; a first bulk-repair approach was reported unsuccessful before exact local repairs.' @(
  (New-Cause 'source_fact' 'Worker identified the same JavaScript escape class during structural line inventory.'),
  (New-Cause 'computation' 'All four damaged and repaired hashes are retained in CJK-KO-P41-002.')
) @(
  (New-Attempt 'Accept first-return hashes.' 'Rejected because bytes were mechanically damaged.' 'rejected'),
  (New-Attempt 'First bulk repair.' 'Failed; detailed transient output was not preserved by the worker, which is retained as evidence limitation.' 'failed'),
  (New-Attempt 'Exact per-file apply_patch delimiter restoration.' 'Accepted; wording unchanged and new hashes frozen.' 'accepted')
) @('Do not erase first-return hashes.','Do not invent the missing transient bulk-repair output.') 'resolved' 'Final repaired identities supersede damaged bytes only; both states remain in the ledger.' @(
  (New-Evidence 'decision_log' 'Exact before/after identities and repair scope.' '${PUBLIC_INTERLANGUAGE_ROOT}/03_projects/language_management/cjk/00_lane_control/CJK_DECISION_LOGBOOK_20260718.md' $null)
) 'Repeated serialization paths can recreate the same defect; failed bulk-repair diagnostics are incomplete.' @('target byte increase equals restored delimiters','worker sees plain parentheses around symbols','bulk replacement lacks exact scope') 'not_applicable' 'not_applicable' @('CJK-KO-P41-002') @('NOE-P41-KO-U05','NOE-P41-KO-U06','NOE-P41-KO-U07','NOE-P41-KO-U08') 'Freeze and retain both damaged and repaired hashes; scope repairs to mechanical serialization only.' 'Recur on any TeX target whose first write used unescaped JavaScript strings.'

Add-Record $allUnits (New-Authority $allUnits @('producer metadata choices file')) @(
  (New-Target 'CHOICES-FINAL' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'metadata_write_failure' 'Markdown TeX delimiters in the terminology evidence file.' @('source_fact','computation') 'The first choices-file patch used a normal JavaScript string and stripped backslashes from several Markdown math spans.' @(
  (New-Cause 'source_fact' 'Root observed forms such as (mathfrak G^*) after the write.'),
  (New-Cause 'computation' 'Repair preceded hashing, so no failed-file hash exists.')
) @(
  (New-Attempt 'Keep malformed Markdown math.' 'Rejected.' 'rejected'),
  (New-Attempt 'Restore exact delimiters with apply_patch and then hash.' 'Accepted.' 'accepted')
) @('Do not conflate metadata formatting repair with target review.','Do not fabricate a failed hash.') 'resolved' 'Final choices file is frozen at 46AF7C...; target TeX was not changed.' @(
  (New-Evidence 'producer_choices' 'Repaired metadata identity.' "$root/TRANSLATION_CHOICES_U01_U12.md" '46AF7CB85AC6775444EE3B37AF3E561A061D3D7F9137AD8F2385F024391821CD')
) 'The same serialization bug affects Markdown containing TeX as well as TeX targets.' @('Markdown math loses backslash','normal JS string contains TeX','metadata looks readable but math markup is gone') 'not_applicable' 'not_applicable' @('CJK-KO-P41-002') @('NOE-P41-KO-WORK-001') 'Apply the same escape discipline to evidence metadata as to target TeX.' 'Recur whenever Markdown evidence embeds TeX through JavaScript strings.'

Add-Record $allUnits (New-Authority $allUnits @('metadata hash and continuation inventory commands')) @(
  (New-Target 'STATUS' "$root/STATUS.md" 'AAC5018E091A871291A661BCA87FFE802102FA1A7716338B8F188DFDA0F8A9C6')
) 'tooling_failure' 'PowerShell foreach output piped directly to another command.' @('source_fact','computation') 'Two bounded metadata commands failed at parse time with An empty pipe element is not allowed.' @(
  (New-Cause 'source_fact' 'PowerShell rejected a pipeline immediately following a foreach statement.'),
  (New-Cause 'computation' 'Failure occurred before any write; repaired command used an explicit output array.')
) @(
  (New-Attempt 'foreach { object } | ConvertTo-Json.' 'Failed at parse time.' 'failed'),
  (New-Attempt 'Collect into task-specific array, then pipe the array.' 'Accepted and returned hashes.' 'accepted')
) @('Do not erase repeated parser failures because later commands succeed.') 'resolved' 'Use explicit collection before projection in bounded PowerShell metadata commands.' @(
  (New-Evidence 'command_history' 'Repeated parser failure described in lane production record.' $null $null)
) 'The idiom can recur in future metadata and inventory commands.' @('foreach statement followed by pipe','empty pipe element parser message','no output file created') 'not_applicable' 'not_applicable' @('CJK-KO-P41-002') @('NOE-P41-KO-WORK-001') 'A successful retry does not erase a recurrent tooling pattern; encode the safe command shape.' 'Recur on the next direct foreach-to-pipeline command.'

Add-Record $allUnits (New-Authority $allUnits @('structural index generation')) @(
  (New-Target 'STRUCTURAL-BUILDER' "$root/evidence/structural_index/build_and_validate_structural_index.ps1" '26F7DCBFE1F9D407A9845BD331F02B60D4D7026F5B389C130B4CC50F5852FC85'),
  (New-Target 'STRUCTURAL-REPORT' "$root/evidence/structural_index/PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json" '38E0F3E3B5CC2552863F9A2970F5424F4E03D0059156F5DF4759242F5A06E751')
) 'tooling_failure' 'PowerShell variable immediately followed by colon in structural-builder diagnostics.' @('source_fact','computation') 'The first structural builder run failed with a parser error on $unit: before generated output was accepted.' @(
  (New-Cause 'source_fact' 'PowerShell parsed the colon as part of an invalid variable reference.'),
  (New-Cause 'computation' 'Changing only $unit: to ${unit}: allowed the same builder to run; deterministic rerun reproduced hashes.')
) @(
  (New-Attempt 'Use unbraced variable before colon.' 'Failed at parse time.' 'failed'),
  (New-Attempt 'Brace the variable and rerun.' 'Accepted; 129/129 records passed.' 'accepted')
) @('Do not treat a metadata validator pass as translation validation.') 'resolved' 'Braced interpolation repaired the builder; generated index/report are current.' @(
  (New-Evidence 'structural_report' 'PASS 129/129, latest NOE-P41-KO-U12-RECEIPT-001.' "$root/evidence/structural_index/PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json" '38E0F3E3B5CC2552863F9A2970F5424F4E03D0059156F5DF4759242F5A06E751')
) 'Similar diagnostic strings can fail before validators run.' @('PowerShell variable followed by colon','parser failure before output','validator report absent') 'not_applicable' 'not_applicable' @('CJK-KO-P41-002','CJK-KO-P41-004') @('NOE-P41-KO-WORK-001','NOE-P41-KO-U12-RECEIPT-001') 'Validator failures belong in the same append-only history they are designed to protect.' 'Recur if a future PowerShell diagnostic interpolates an unbraced variable before punctuation.'

Add-Record $allUnits (New-Authority $allUnits @('difficulty-ledger initialization and hash-chain validation')) @(
  (New-Target 'INITIAL-FAILED-JSONL' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_20260804.jsonl" 'DBF7313F2600D05809897579052213BF9B6658939219CC8FE568971F938CFE8B'),
  (New-Target 'INITIAL-FAILED-CSV' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_20260804.csv" '9E3336E8D7F0CCE4D5A66A397A36CBFEFDC59442BF4CCC2706E97BBA89FEE697'),
  (New-Target 'INITIAL-FAIL-REPORT' "$root/evidence/difficulty/DIFFICULTY_LEDGER_VALIDATION_REPORT_INITIAL_FAIL_20260804.json" '7852762AB945721AA34B812E1A6211C9DD5EFECE79A7B4D571ED15591BEFAD77')
) 'tooling_failure' 'PowerShell function scope prevented the ledger initializer from carrying the predecessor hash between Add-Record calls.' @('source_fact','computation') 'Initial validation found valid record self-hashes but predecessor-hash mismatches on records 002 through 012.' @(
  (New-Cause 'computation' 'Assignment to $previous inside Add-Record created a function-local value, leaving the outer value null for every later call.'),
  (New-Cause 'source_fact' 'The preserved FAIL report lists eleven previous hash mismatch errors and no self-hash errors.')
) @(
  (New-Attempt 'Generate records with an unscoped $previous variable.' 'Twelve records were generated, but validation failed the predecessor chain for records 002-012.' 'failed'),
  (New-Attempt 'Preserve the failed JSONL, CSV, and validation report; change only the chain variable to script scope; regenerate the intended ledger with this failure recorded.' 'Accepted for a deterministic validation rerun.' 'accepted')
) @('Do not discard the invalid first ledger merely because a corrected projection is available.','Do not present self-hash success as hash-chain success.') 'resolved' 'The invalid initial artifacts are immutable evidence; the corrected canonical ledger records this failure as CJK-KO-P41-HARD-013.' @(
  (New-Evidence 'failed_jsonl' 'Initial invalid predecessor chain.' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_20260804.jsonl" 'DBF7313F2600D05809897579052213BF9B6658939219CC8FE568971F938CFE8B'),
  (New-Evidence 'failed_csv' 'Initial projection paired to the invalid chain.' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_20260804.csv" '9E3336E8D7F0CCE4D5A66A397A36CBFEFDC59442BF4CCC2706E97BBA89FEE697'),
  (New-Evidence 'validation_report' 'Machine FAIL report.' "$root/evidence/difficulty/DIFFICULTY_LEDGER_VALIDATION_REPORT_INITIAL_FAIL_20260804.json" '7852762AB945721AA34B812E1A6211C9DD5EFECE79A7B4D571ED15591BEFAD77')
) 'The initializer is reproducible, but any future scope refactor can reintroduce the same chain break.' @('all previous_record_sha256 values null','self hashes pass while predecessor chain fails','blank chain-head status output') 'not_applicable' 'not_applicable' @('CJK-KO-P41-002','CJK-KO-P41-004') @('NOE-P41-KO-WORK-001') 'Validate both record self-hashes and linkage; preserve the first failed output before rebuilding an initialization artifact.' 'Revisit if the ledger initializer, hash algorithm, or serialization order changes.'

Add-Record $allUnits (New-Authority $allUnits @('difficulty-ledger append-only initialization guard')) @(
  (New-Target 'INITIAL-FAILED-ACTIVE-JSONL' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_active_20260804.jsonl" 'DBF7313F2600D05809897579052213BF9B6658939219CC8FE568971F938CFE8B'),
  (New-Target 'INITIAL-FAILED-ACTIVE-CSV' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_active_20260804.csv" '9E3336E8D7F0CCE4D5A66A397A36CBFEFDC59442BF4CCC2706E97BBA89FEE697')
) 'tooling_failure' 'The corrected initializer was invoked while the invalid canonical ledger still occupied the append-only output path.' @('source_fact','computation') 'The initializer stopped at line 4 with Append-only ledger already exists before writing corrected bytes.' @(
  (New-Cause 'source_fact' 'The initializer deliberately refuses to overwrite an existing ledger.'),
  (New-Cause 'computation' 'The invalid first output had been copied for preservation but not moved away from the canonical output path.')
) @(
  (New-Attempt 'Rerun corrected initializer against occupied canonical paths.' 'Blocked by append-only guard; no corrected output was written.' 'failed'),
  (New-Attempt 'Move the invalid active JSONL and CSV to explicit failure paths within the same evidence directory, retain earlier copies, then initialize new canonical paths.' 'Accepted without deleting evidence.' 'accepted')
) @('Do not disable the append-only guard to make regeneration convenient.','Do not delete the invalid active output.') 'resolved' 'The guard failure is retained here; the invalid active files remain byte-identical under explicit failure names.' @(
  (New-Evidence 'command_failure' 'Initializer line 4 emitted Append-only ledger already exists; no file was changed by the blocked run.' $null $null),
  (New-Evidence 'preserved_jsonl' 'Moved invalid active JSONL.' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_active_20260804.jsonl" 'DBF7313F2600D05809897579052213BF9B6658939219CC8FE568971F938CFE8B'),
  (New-Evidence 'preserved_csv' 'Moved invalid active CSV.' "$root/evidence/difficulty/difficulty_ledger_initial_chain_fail_active_20260804.csv" '9E3336E8D7F0CCE4D5A66A397A36CBFEFDC59442BF4CCC2706E97BBA89FEE697')
) 'A future repair may again encounter an occupied canonical path; the guard must remain strict.' @('Append-only ledger already exists','initializer exits before generation','temptation to delete or overwrite evidence') 'not_applicable' 'not_applicable' @('CJK-KO-P41-002','CJK-KO-P41-004') @('NOE-P41-KO-WORK-001') 'Treat an append-only guard as evidence-preservation behavior, then move invalid initialization artifacts under stable failure names before rebuilding.' 'Revisit whenever initialization output paths already exist.'

$lines = @($records | ForEach-Object { $_.Line })
[IO.File]::WriteAllText($ledgerPath, (($lines -join "`n") + "`n"), [Text.UTF8Encoding]::new($false))
$csvRows = foreach ($r in $records) {
  $o = $r.Object
  [pscustomobject]@{
    record_id=$o.record_id; append_sequence=$o.append_sequence; recorded_at=$o.recorded_at; unit_ids=($o.unit_ids -join ';')
    category=$o.category; resolution_state=$o.resolution_state; symptom=$o.symptom; residual_risk=$o.residual_risk
    mandarin_simplified_dominance_risk=$o.mandarin_simplified_dominance_risk; lexical_attractor_basin=$o.lexical_attractor_basin
    related_decision_ids=($o.related_decision_ids -join ';'); related_structural_ids=($o.related_structural_ids -join ';')
    previous_record_sha256=$o.previous_record_sha256; record_sha256=$r.Hash; review_state=$o.review_state; revisit_condition=$o.revisit_condition
  }
}
$csvRows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8
Write-Output "created $($records.Count) append-only records; chain head $script:previous"
