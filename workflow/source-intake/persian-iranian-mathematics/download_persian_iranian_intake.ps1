param(
  [string]$OutDir = (Join-Path $PSScriptRoot 'downloaded_sources'),
  [switch]$IncludePageImages,
  [switch]$IncludeSupportTools
)
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
function Fetch($Url, $Name) {
  if ([string]::IsNullOrWhiteSpace($Url)) { return }
  $Dest = Join-Path $OutDir $Name
  if (Test-Path -LiteralPath $Dest) { Write-Host "exists $Name"; return }
  Write-Host "download $Name"
  try {
    Invoke-WebRequest -Uri $Url -OutFile $Dest
  } catch {
    Write-Warning "failed $Name :: $($_.Exception.Message)"
    if (Test-Path -LiteralPath $Dest) { Remove-Item -LiteralPath $Dest -Force }
  }
}

# 1 - Abu Rayhan al-Biruni - al-Qanun al-Masudi
# https://archive.org/details/al-qanun-al-masudi-biruni-muhammad-ibn-ahmad
Fetch "https://archive.org/download/al-qanun-al-masudi-biruni-muhammad-ibn-ahmad/al-Qan%C5%ABn%20al-Mas%CA%BF%C5%ABd%C4%AB%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D9%85%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%20B%C4%ABr%C5%ABn%C4%AB%2C%20Mu%E1%B8%A5ammad%20ibn%20A%E1%B8%A5mad%20%D8%A8%D9%8A%D8%B1%D9%88%D9%86%D9%8A%D8%8C%20%D9%85%D8%AD%D9%85%D8%AF%20%D8%A8%D9%86%20%D8%A3%D8%AD%D9%85%D8%AF.pdf" "Abu Rayhan al-Biruni - al-Qanun al-Masudi.pdf"
Fetch "https://archive.org/download/al-qanun-al-masudi-biruni-muhammad-ibn-ahmad/al-Qan%C5%ABn%20al-Mas%CA%BF%C5%ABd%C4%AB%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D9%85%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%20B%C4%ABr%C5%ABn%C4%AB%2C%20Mu%E1%B8%A5ammad%20ibn%20A%E1%B8%A5mad%20%D8%A8%D9%8A%D8%B1%D9%88%D9%86%D9%8A%D8%8C%20%D9%85%D8%AD%D9%85%D8%AF%20%D8%A8%D9%86%20%D8%A3%D8%AD%D9%85%D8%AF_djvu.txt" "Abu Rayhan al-Biruni - al-Qanun al-Masudi.djvu.txt"
Fetch "https://archive.org/download/al-qanun-al-masudi-biruni-muhammad-ibn-ahmad/al-Qan%C5%ABn%20al-Mas%CA%BF%C5%ABd%C4%AB%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D9%85%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%20B%C4%ABr%C5%ABn%C4%AB%2C%20Mu%E1%B8%A5ammad%20ibn%20A%E1%B8%A5mad%20%D8%A8%D9%8A%D8%B1%D9%88%D9%86%D9%8A%D8%8C%20%D9%85%D8%AD%D9%85%D8%AF%20%D8%A8%D9%86%20%D8%A3%D8%AD%D9%85%D8%AF_djvu.xml" "Abu Rayhan al-Biruni - al-Qanun al-Masudi.djvu.xml"
Fetch "https://archive.org/download/al-qanun-al-masudi-biruni-muhammad-ibn-ahmad/al-Qan%C5%ABn%20al-Mas%CA%BF%C5%ABd%C4%AB%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D9%85%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%20B%C4%ABr%C5%ABn%C4%AB%2C%20Mu%E1%B8%A5ammad%20ibn%20A%E1%B8%A5mad%20%D8%A8%D9%8A%D8%B1%D9%88%D9%86%D9%8A%D8%8C%20%D9%85%D8%AD%D9%85%D8%AF%20%D8%A8%D9%86%20%D8%A3%D8%AD%D9%85%D8%AF_scandata.xml" "Abu Rayhan al-Biruni - al-Qanun al-Masudi.scandata.xml"
if ($IncludePageImages) { Fetch "https://archive.org/download/al-qanun-al-masudi-biruni-muhammad-ibn-ahmad/al-Qan%C5%ABn%20al-Mas%CA%BF%C5%ABd%C4%AB%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%A7%D9%84%D9%85%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%20B%C4%ABr%C5%ABn%C4%AB%2C%20Mu%E1%B8%A5ammad%20ibn%20A%E1%B8%A5mad%20%D8%A8%D9%8A%D8%B1%D9%88%D9%86%D9%8A%D8%8C%20%D9%85%D8%AD%D9%85%D8%AF%20%D8%A8%D9%86%20%D8%A3%D8%AD%D9%85%D8%AF_jp2.zip" "Abu Rayhan al-Biruni - al-Qanun al-Masudi.jp2.zip" }

# 1 - Nasir al-Din al-Tusi - Tahrir-i Uqlidis / Tahrir Euclid
# https://archive.org/details/in.ernet.dli.2015.361025
Fetch "https://archive.org/download/in.ernet.dli.2015.361025/2015.361025.Tahrir-E.pdf" "Nasir al-Din al-Tusi - Tahrir-i Uqlidis _ Tahrir Euclid.pdf"
Fetch "https://archive.org/download/in.ernet.dli.2015.361025/2015.361025.Tahrir-E_djvu.txt" "Nasir al-Din al-Tusi - Tahrir-i Uqlidis _ Tahrir Euclid.djvu.txt"
Fetch "https://archive.org/download/in.ernet.dli.2015.361025/2015.361025.Tahrir-E_djvu.xml" "Nasir al-Din al-Tusi - Tahrir-i Uqlidis _ Tahrir Euclid.djvu.xml"
Fetch "https://archive.org/download/in.ernet.dli.2015.361025/2015.361025.Tahrir-E_scandata.xml" "Nasir al-Din al-Tusi - Tahrir-i Uqlidis _ Tahrir Euclid.scandata.xml"
if ($IncludePageImages) { Fetch "https://archive.org/download/in.ernet.dli.2015.361025/2015.361025.Tahrir-E_jp2.zip" "Nasir al-Din al-Tusi - Tahrir-i Uqlidis _ Tahrir Euclid.jp2.zip" }

# 1 - Omar Khayyam - Treatise on Algebra / Sina'at al-jabr wa-al-muqabalah
# https://archive.org/details/ldpd_15264441_000
Fetch "https://archive.org/download/ldpd_15264441_000/ldpd_15264441_000.pdf" "Omar Khayyam - Treatise on Algebra _ Sina_at al-jabr wa-al-muqabalah.pdf"
Fetch "https://archive.org/download/ldpd_15264441_000/ldpd_15264441_000_djvu.txt" "Omar Khayyam - Treatise on Algebra _ Sina_at al-jabr wa-al-muqabalah.djvu.txt"
Fetch "https://archive.org/download/ldpd_15264441_000/ldpd_15264441_000_djvu.xml" "Omar Khayyam - Treatise on Algebra _ Sina_at al-jabr wa-al-muqabalah.djvu.xml"
Fetch "https://archive.org/download/ldpd_15264441_000/ldpd_15264441_000_scandata.xml" "Omar Khayyam - Treatise on Algebra _ Sina_at al-jabr wa-al-muqabalah.scandata.xml"
if ($IncludePageImages) { Fetch "https://archive.org/download/ldpd_15264441_000/ldpd_15264441_000_jp2.zip" "Omar Khayyam - Treatise on Algebra _ Sina_at al-jabr wa-al-muqabalah.jp2.zip" }

# 1 - Jamshid al-Kashi - Miftah al-Hisab
# https://archive.org/details/dli.ministry.26383
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-1%2529.pdf" "Jamshid al-Kashi - Miftah al-Hisab part 1.pdf"
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-2%2529.pdf" "Jamshid al-Kashi - Miftah al-Hisab part 2.pdf"
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-1%2529_djvu.txt" "Jamshid al-Kashi - Miftah al-Hisab part 1.djvu.txt"
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-2%2529_djvu.txt" "Jamshid al-Kashi - Miftah al-Hisab part 2.djvu.txt"
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-1%2529_djvu.xml" "Jamshid al-Kashi - Miftah al-Hisab part 1.djvu.xml"
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-2%2529_djvu.xml" "Jamshid al-Kashi - Miftah al-Hisab part 2.djvu.xml"
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-1%2529_scandata.xml" "Jamshid al-Kashi - Miftah al-Hisab part 1.scandata.xml"
Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-2%2529_scandata.xml" "Jamshid al-Kashi - Miftah al-Hisab part 2.scandata.xml"
if ($IncludePageImages) { Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-1%2529_jp2.zip" "Jamshid al-Kashi - Miftah al-Hisab part 1.jp2.zip" }
if ($IncludePageImages) { Fetch "https://archive.org/download/dli.ministry.26383/19556.12873-%2520%2528part-2%2529_jp2.zip" "Jamshid al-Kashi - Miftah al-Hisab part 2.jp2.zip" }

# 2 - Nasir al-Din al-Tusi - Shakl al-Qatta / Treatise on the Complete Quadrilateral
# https://archive.org/details/11921309pdf2282
Fetch "https://archive.org/download/11921309pdf2282/1192%20-%20%D9%83%D8%AA%D8%A7%D8%A8%20%D8%B4%D9%83%D9%84%20%D8%A7%D9%84%D9%82%D8%B7%D8%A7%D8%B9%20-%20%D8%A7%D9%84%D9%82%D8%B3%D8%B7%D9%86%D8%B7%D9%8A%D9%86%D9%8A%D8%A9%20-%201309%20%D9%83%D8%AA%D8%A7%D8%A8%20%D8%B5%D9%8A%D8%BA%D8%A9%20%D8%A8%D9%8A%20%D8%AF%D9%8A%20%D8%A7%D9%81%20%D8%A7%D9%82%D8%B1%D8%A7%20%D8%A7%D9%88%D9%86%D9%84%D8%A7%D9%8A%D9%86%20%20pdf%20%20%20%20%202282.pdf" "Nasir al-Din al-Tusi - Shakl al-Qatta _ Treatise on the Complete Quadrilateral.pdf"

# 2 - Nasir al-Din al-Tusi - Tahrir al-Majisti / Almagest recension
# https://archive.org/details/dli.ministry.27192
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-1%2529.pdf" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 1.pdf"
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-2%2529.pdf" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 2.pdf"
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-1%2529_djvu.txt" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 1.djvu.txt"
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-2%2529_djvu.txt" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 2.djvu.txt"
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-1%2529_djvu.xml" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 1.djvu.xml"
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-2%2529_djvu.xml" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 2.djvu.xml"
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-1%2529_scandata.xml" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 1.scandata.xml"
Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-2%2529_scandata.xml" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 2.scandata.xml"
if ($IncludePageImages) { Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-1%2529_jp2.zip" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 1.jp2.zip" }
if ($IncludePageImages) { Fetch "https://archive.org/download/dli.ministry.27192/19558.12875-%2520%2528part-2%2529_jp2.zip" "Nasir al-Din al-Tusi - Tahrir al-Majisti _ Almagest recension part 2.jp2.zip" }

# 2 - Abu Rayhan al-Biruni - Elements of Astrology / Kitab al-Tafhim-related English source
# https://archive.org/details/al-birini-elementsof-astrology
Fetch "https://archive.org/download/al-birini-elementsof-astrology/AlBiriniElementsofAstrology.pdf" "Abu Rayhan al-Biruni - Elements of Astrology _ Kitab al-Tafhim-related English source.pdf"
Fetch "https://archive.org/download/al-birini-elementsof-astrology/AlBiriniElementsofAstrology_djvu.txt" "Abu Rayhan al-Biruni - Elements of Astrology _ Kitab al-Tafhim-related English source.djvu.txt"
Fetch "https://archive.org/download/al-birini-elementsof-astrology/AlBiriniElementsofAstrology_djvu.xml" "Abu Rayhan al-Biruni - Elements of Astrology _ Kitab al-Tafhim-related English source.djvu.xml"
Fetch "https://archive.org/download/al-birini-elementsof-astrology/AlBiriniElementsofAstrology_scandata.xml" "Abu Rayhan al-Biruni - Elements of Astrology _ Kitab al-Tafhim-related English source.scandata.xml"
if ($IncludePageImages) { Fetch "https://archive.org/download/al-birini-elementsof-astrology/AlBiriniElementsofAstrology_jp2.zip" "Abu Rayhan al-Biruni - Elements of Astrology _ Kitab al-Tafhim-related English source.jp2.zip" }

# 3 - John Tytler - Analysis and Specimens of a Persian Work on Mathematics and Astronomy
# https://archive.org/details/jstor-25207498
Fetch "https://archive.org/download/jstor-25207498/25207498.pdf" "John Tytler - Analysis and Specimens of a Persian Work on Mathematics and Astronomy.pdf"
Fetch "https://archive.org/download/jstor-25207498/25207498_djvu.txt" "John Tytler - Analysis and Specimens of a Persian Work on Mathematics and Astronomy.djvu.txt"
Fetch "https://archive.org/download/jstor-25207498/25207498_djvu.xml" "John Tytler - Analysis and Specimens of a Persian Work on Mathematics and Astronomy.djvu.xml"
Fetch "https://archive.org/download/jstor-25207498/25207498_scandata.xml" "John Tytler - Analysis and Specimens of a Persian Work on Mathematics and Astronomy.scandata.xml"
if ($IncludePageImages) { Fetch "https://archive.org/download/jstor-25207498/25207498_jp2.zip" "John Tytler - Analysis and Specimens of a Persian Work on Mathematics and Astronomy.jp2.zip" }

# 3 - Gholamreza Mokhtari Aski - Descriptive Persian-English Dictionary of Basic Mathematics
# https://archive.org/details/descriptivepersianenglishdictionaryofbasicmathematics
if ($IncludeSupportTools) {
  Fetch "https://archive.org/download/descriptivepersianenglishdictionaryofbasicmathematics/descriptive%20%20Persian-English%20%20dictionary%20of%20basic%20Mathematics.pdf" "Gholamreza Mokhtari Aski - Descriptive Persian-English Dictionary of Basic Mathematics.pdf"
  Fetch "https://archive.org/download/descriptivepersianenglishdictionaryofbasicmathematics/descriptive%20%20Persian-English%20%20dictionary%20of%20basic%20Mathematics_djvu.txt" "Gholamreza Mokhtari Aski - Descriptive Persian-English Dictionary of Basic Mathematics.djvu.txt"
  Fetch "https://archive.org/download/descriptivepersianenglishdictionaryofbasicmathematics/descriptive%20%20Persian-English%20%20dictionary%20of%20basic%20Mathematics_djvu.xml" "Gholamreza Mokhtari Aski - Descriptive Persian-English Dictionary of Basic Mathematics.djvu.xml"
  Fetch "https://archive.org/download/descriptivepersianenglishdictionaryofbasicmathematics/descriptive%20%20Persian-English%20%20dictionary%20of%20basic%20Mathematics_scandata.xml" "Gholamreza Mokhtari Aski - Descriptive Persian-English Dictionary of Basic Mathematics.scandata.xml"
  if ($IncludePageImages) { Fetch "https://archive.org/download/descriptivepersianenglishdictionaryofbasicmathematics/descriptive%20%20Persian-English%20%20dictionary%20of%20basic%20Mathematics_jp2.zip" "Gholamreza Mokhtari Aski - Descriptive Persian-English Dictionary of Basic Mathematics.jp2.zip" }
}

# 3 - M. Heydari-Malayeri - Etymological Dictionary of Astronomy and Astrophysics: English-French-Persian
# https://archive.org/details/arxiv-astro-ph0701421
if ($IncludeSupportTools) {
  Fetch "https://archive.org/download/arxiv-astro-ph0701421/astro-ph0701421.pdf" "M. Heydari-Malayeri - Etymological Dictionary of Astronomy and Astrophysics_ English-French-Persian.pdf"
  Fetch "https://archive.org/download/arxiv-astro-ph0701421/astro-ph0701421_djvu.txt" "M. Heydari-Malayeri - Etymological Dictionary of Astronomy and Astrophysics_ English-French-Persian.djvu.txt"
  Fetch "https://archive.org/download/arxiv-astro-ph0701421/astro-ph0701421_djvu.xml" "M. Heydari-Malayeri - Etymological Dictionary of Astronomy and Astrophysics_ English-French-Persian.djvu.xml"
  Fetch "https://archive.org/download/arxiv-astro-ph0701421/astro-ph0701421_scandata.xml" "M. Heydari-Malayeri - Etymological Dictionary of Astronomy and Astrophysics_ English-French-Persian.scandata.xml"
  if ($IncludePageImages) { Fetch "https://archive.org/download/arxiv-astro-ph0701421/astro-ph0701421_jp2.zip" "M. Heydari-Malayeri - Etymological Dictionary of Astronomy and Astrophysics_ English-French-Persian.jp2.zip" }
}

# open - Ulugh Beg / Samarkand observatory tradition - Zij-i Sultani / star catalogue tradition
# https://archive.org/details/arxiv-1206.0628
Fetch "https://archive.org/download/arxiv-1206.0628/1206.0628.pdf" "Ulugh Beg _ Samarkand observatory tradition - Zij-i Sultani _ star catalogue tradition.pdf"
