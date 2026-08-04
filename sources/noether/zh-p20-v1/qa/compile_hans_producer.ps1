$ErrorActionPreference = 'Stop'
$workspace='C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper20_zh_translation_001_20260722'
$targetDir=Join-Path $workspace 'zh-Hans-CN'
$texName='Noether_Paper20_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex'
$texPath=Join-Path $targetDir $texName
$base=[IO.Path]::GetFileNameWithoutExtension($texName)
$utf8=[Text.UTF8Encoding]::new($false)
if(-not(Test-Path -LiteralPath $texPath)){throw "Missing Hans TeX: $texPath"}
$passes=@()
for($pass=1;$pass-le2;$pass++){
  $out=Join-Path $targetDir ("{0}.pass{1}.stdout.txt" -f $base,$pass)
  Push-Location $targetDir
  try{& xelatex -interaction=nonstopmode -halt-on-error -file-line-error $texName 2>&1|Tee-Object -FilePath $out;$code=$LASTEXITCODE}finally{Pop-Location}
  $passes += [ordered]@{pass=$pass;exit_code=$code;stdout_path=[IO.Path]::GetFileName($out)}
  if($code-ne0){throw "XeLaTeX pass $pass failed with exit code $code"}
}
$pdf=Join-Path $targetDir "$base.pdf";$log=Join-Path $targetDir "$base.log"
if(-not(Test-Path -LiteralPath $pdf)){throw 'Expected PDF missing'};if(-not(Test-Path -LiteralPath $log)){throw 'Expected log missing'}
function Meta([string]$path){$f=Get-Item -LiteralPath $path;[ordered]@{path=$path.Substring($workspace.Length+1).Replace('\','/');bytes=$f.Length;sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash}}
$text=[IO.File]::ReadAllText($log);$pm=[regex]::Match($text,'\((\d+) pages?')
$record=[ordered]@{
  record_type='producer_mechanical_build';work_unit='Noether Paper 20';target_label='zh-Hans-CN';recorded_local_time=(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz');compiler='XeLaTeX';passes=$passes;
  tex=Meta $texPath;pdf=(Meta $pdf)+[ordered]@{pages_reported_by_log=if($pm.Success){[int]$pm.Groups[1].Value}else{$null};opened_or_rendered_by_producer=$false};
  log=(Meta $log)+[ordered]@{error_pattern_matches=([regex]::Matches($text,'(?m)^!|Emergency stop|Fatal error')).Count;warning_line_matches=([regex]::Matches($text,'(?m)^.*Warning.*$')).Count;overfull_matches=([regex]::Matches($text,'Overfull')).Count;underfull_matches=([regex]::Matches($text,'Underfull')).Count};
  epistemic_boundary=[ordered]@{compilation_success_is_translation_validation=$false;source_check_performed=$false;semantic_or_formula_check_performed=$false;translation_quality_check_performed=$false;visual_check_performed=$false;independent_check='pending'}
}
[IO.File]::WriteAllText((Join-Path $workspace 'qa\HANS_MECHANICAL_BUILD_RECORD.json'),($record|ConvertTo-Json -Depth 8),$utf8)
$record|ConvertTo-Json -Depth 8

