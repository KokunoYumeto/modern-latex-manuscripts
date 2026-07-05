param(
  [string]$RepoRoot = "C:\Users\Floris\Documents\Papors\modern-latex-manuscripts-github",
  [string]$Stamp = "20260705"
)

Add-Type -AssemblyName System.IO.Compression.FileSystem

$ErrorActionPreference = "Stop"

$zipRoots = @(
  "interlanguage-sidecar\20260704\latex_source_body_bundles",
  "noether-source-corpus-provenance\20260704",
  "noether-slavic-source-canon\20260704"
)

$outDir = Join-Path $RepoRoot "manifests\source-intake"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$texPattern = '\.(tex|ltx|cls|sty|bib)$'
$languageCodes = @(
  "ar","az","be","bg","bs","ca","cnr","cs","de","dsb","en","es","fa","fr","gl","he","hr",
  "hsb","id","it","ja","kk","ko","ky","la","mk","ms","oc","pl","ps","pt","ro","ru","sh",
  "sk","sl","sr","sw","tk","tr","uk","ur","uz","zh"
)

$wordHints = [ordered]@{
  "german" = "de"
  "deutsch" = "de"
  "english" = "en"
  "spanish" = "es"
  "espanol" = "es"
  "francais" = "fr"
  "french" = "fr"
  "japanese" = "ja"
  "chinese" = "zh"
  "arabic" = "ar"
  "persian" = "fa"
  "farsi" = "fa"
  "tajik" = "fa"
  "ukrainian" = "uk"
  "russian" = "ru"
  "belarusian" = "be"
  "bulgarian" = "bg"
  "croatian" = "hr"
  "serbian" = "sr"
  "bosnian" = "bs"
  "slovene" = "sl"
  "slovenian" = "sl"
  "slovak" = "sk"
  "czech" = "cs"
  "polish" = "pl"
  "macedonian" = "mk"
  "sorbian" = "hsb"
  "interslavic" = "isv"
  "slavic" = "slavic"
  "romance" = "romance"
  "cjk" = "cjk"
}

function Get-RelativePath([string]$Base, [string]$Path) {
  $baseUri = [Uri]((Resolve-Path $Base).Path.TrimEnd('\') + '\')
  $pathUri = [Uri]((Resolve-Path $Path).Path)
  return [Uri]::UnescapeDataString($baseUri.MakeRelativeUri($pathUri).ToString()).Replace('/', '\')
}

function Get-LanguageHint([string]$EntryPath, [string]$ZipName) {
  $path = $EntryPath.Replace('\','/')
  $segments = $path -split '/'
  foreach ($seg in $segments) {
    $s = $seg.ToLowerInvariant()
    if ($languageCodes -contains $s) { return $s }
  }
  foreach ($seg in $segments) {
    $tokens = $seg.ToLowerInvariant() -split '[^a-z]+'
    foreach ($tok in $tokens) {
      if ($languageCodes -contains $tok) { return $tok }
    }
  }
  $combined = ($ZipName + " " + $EntryPath).ToLowerInvariant()
  foreach ($k in $wordHints.Keys) {
    if ($combined.Contains($k)) { return $wordHints[$k] }
  }
  return "unknown"
}

$zipPaths = foreach ($root in $zipRoots) {
  $p = Join-Path $RepoRoot $root
  if (Test-Path $p) {
    Get-ChildItem -Path $p -Recurse -File -Filter *.zip
  }
}

$packageRows = New-Object System.Collections.Generic.List[object]
$languageRows = New-Object System.Collections.Generic.List[object]
$jsonPackages = New-Object System.Collections.Generic.List[object]
$seenSha = @{}

foreach ($zipFile in ($zipPaths | Sort-Object FullName -Unique)) {
  $zip = [IO.Compression.ZipFile]::OpenRead($zipFile.FullName)
  try {
    $texEntries = @($zip.Entries | Where-Object { $_.FullName -match $texPattern })
    if ($texEntries.Count -eq 0) { continue }

    $rel = Get-RelativePath $RepoRoot $zipFile.FullName
    $sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $zipFile.FullName).Hash
    $isDuplicate = $seenSha.ContainsKey($sha)
    $duplicateOf = ""
    if ($isDuplicate) {
      $duplicateOf = $seenSha[$sha]
    } else {
      $seenSha[$sha] = $rel
    }
    $langCounts = @{}
    $samplesByLang = @{}

    foreach ($entry in $texEntries) {
      $lang = Get-LanguageHint $entry.FullName $zipFile.Name
      if (-not $langCounts.ContainsKey($lang)) {
        $langCounts[$lang] = 0
        $samplesByLang[$lang] = New-Object System.Collections.Generic.List[string]
      }
      $langCounts[$lang]++
      if ($samplesByLang[$lang].Count -lt 5) {
        $samplesByLang[$lang].Add($entry.FullName)
      }
    }

    $packageRows.Add([pscustomobject]@{
      zip_path = $rel
      zip_name = $zipFile.Name
      size_bytes = $zipFile.Length
      sha256 = $sha
      total_zip_entries = $zip.Entries.Count
      tex_like_entries = $texEntries.Count
      language_buckets = (($langCounts.Keys | Sort-Object) -join ';')
      duplicate_sha = $isDuplicate
      duplicate_of = $duplicateOf
    })

    if (-not $isDuplicate) {
      $jsonLangs = @()
      foreach ($lang in ($langCounts.Keys | Sort-Object)) {
        $samples = @($samplesByLang[$lang])
        $languageRows.Add([pscustomobject]@{
          zip_path = $rel
          language_hint = $lang
          tex_like_entries = $langCounts[$lang]
          sample_paths = ($samples -join ' | ')
        })
        $jsonLangs += [pscustomobject]@{
          language_hint = $lang
          tex_like_entries = $langCounts[$lang]
          sample_paths = $samples
        }
      }

      $jsonPackages.Add([pscustomobject]@{
        zip_path = $rel
        zip_name = $zipFile.Name
        size_bytes = $zipFile.Length
        sha256 = $sha
        total_zip_entries = $zip.Entries.Count
        tex_like_entries = $texEntries.Count
        duplicate_sha = $false
        languages = $jsonLangs
      })
    }
  } finally {
    $zip.Dispose()
  }
}

$pkgCsv = Join-Path $outDir "${Stamp}_interlanguage_latex_source_body_inventory_packages.csv"
$langCsv = Join-Path $outDir "${Stamp}_interlanguage_latex_source_body_inventory_language_counts.csv"
$jsonPath = Join-Path $outDir "${Stamp}_interlanguage_latex_source_body_inventory.json"
$mdPath = Join-Path $outDir "${Stamp}_interlanguage_latex_source_body_inventory.md"

$packageRows | Sort-Object zip_path | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $pkgCsv
$languageRows | Sort-Object language_hint, zip_path | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $langCsv
$jsonPackages | ConvertTo-Json -Depth 8 | Set-Content -Encoding UTF8 -Path $jsonPath

$uniquePackageRows = @($packageRows | Where-Object { -not $_.duplicate_sha })
$duplicatePackageRows = @($packageRows | Where-Object { $_.duplicate_sha })
$totalTex = ($uniquePackageRows | Measure-Object -Property tex_like_entries -Sum).Sum
$totalZips = $uniquePackageRows.Count
$overallLang = $languageRows | Group-Object language_hint | ForEach-Object {
  [pscustomobject]@{
    language_hint = $_.Name
    tex_like_entries = (($_.Group | Measure-Object -Property tex_like_entries -Sum).Sum)
    zip_count = $_.Group.Count
  }
} | Sort-Object @{ Expression = "tex_like_entries"; Descending = $true }, language_hint

$md = New-Object System.Collections.Generic.List[string]
$md.Add("# Interlanguage LaTeX Source-Body Inventory ($Stamp)")
$md.Add("")
$md.Add("Machine-readable inventory of ZIP packets containing TeX-family source bodies for the interlanguage/multilingual methodology shelf.")
$md.Add("")
$md.Add("Classification: source-corpus/provenance support only. Not native review, accepted terminology, translation completion, source-fidelity certification, publication readiness, reader output, or critical-edition material.")
$md.Add("")
$md.Add("- Unique ZIP payloads with TeX-like entries: $totalZips")
$md.Add("- Duplicate ZIP paths by SHA256: $($duplicatePackageRows.Count)")
$md.Add("- Total TeX-like entries counted, unique by ZIP SHA256: $totalTex")
$md.Add("- Package CSV: ``$(Split-Path $pkgCsv -Leaf)``")
$md.Add("- Language-count CSV: ``$(Split-Path $langCsv -Leaf)``")
$md.Add("- JSON: ``$(Split-Path $jsonPath -Leaf)``")
$md.Add("")
$md.Add("## Language-Hint Totals")
$md.Add("")
$md.Add("| language_hint | tex_like_entries | zip_count |")
$md.Add("|---|---:|---:|")
foreach ($row in $overallLang) {
  $md.Add("| $($row.language_hint) | $($row.tex_like_entries) | $($row.zip_count) |")
}
$md.Add("")
$md.Add("## Package Totals")
$md.Add("")
$md.Add("| ZIP | TeX-like entries | Size bytes | SHA256 |")
$md.Add("|---|---:|---:|---|")
foreach ($row in ($packageRows | Sort-Object @{ Expression = "tex_like_entries"; Descending = $true }, zip_name)) {
  $dup = if ($row.duplicate_sha) { " duplicate of ``$($row.duplicate_of)``" } else { "" }
  $md.Add("| ``$($row.zip_path)``$dup | $($row.tex_like_entries) | $($row.size_bytes) | ``$($row.sha256)`` |")
}
$md.Add("")
$md.Add("## Current Gap")
$md.Add("")
$md.Add("The inventory confirms a substantial source-body shelf, but the language hints are still uneven and partly heuristic. Several ZIPs are broad Noether/control/source-corpus payloads rather than per-language native mathematical corpora. The next collection pass should target hundreds of independent native mathematical TeX bodies per individual language, especially low-resource Slavic, CJK, Arabic/Persianate, and planned/interlanguage comparison lanes.")

$md -join "`r`n" | Set-Content -Encoding UTF8 -Path $mdPath

Write-Output "Wrote $pkgCsv"
Write-Output "Wrote $langCsv"
Write-Output "Wrote $jsonPath"
Write-Output "Wrote $mdPath"
