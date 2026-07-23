param(
  [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot),
  [int]$RecordId = 21511144,
  [string]$ExpectedManifestPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "tmp\zenodo-sga3-loop2-21511144\successor_upload\09a_RELEASE_FILE_MANIFEST.csv"),
  [string]$ExpectedValidationPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "tmp\zenodo-sga3-loop2-21511144\successor_upload\09b_RELEASE_VALIDATION.json"),
  [string]$PredecessorZipReadbackPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "manifests\published-zenodo\20260723_sga4_reference_v2_r7_record_21510120_zip_member_readback.json"),
  [string]$NewZipPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "sources\sga\sga3-english-expose-v-loop2-native-r2-freeze2-20260723\SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip"),
  [string]$OutputPrefix = (Join-Path (Split-Path -Parent $PSScriptRoot) "manifests\published-zenodo\20260723_sga3_expose_v_loop2_record_21511144")
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
Add-Type -AssemblyName System.IO.Compression.FileSystem

$newZipName = "10c3_SGA3_English_Expose_V_Loop2_Native_Source_Evidence_R2_20260723.zip"
$manifestName = "09a_RELEASE_FILE_MANIFEST.csv"
$validationName = "09b_RELEASE_VALIDATION.json"
$apiUrl = "https://zenodo.org/api/records/$RecordId"
$tempRoot = Join-Path $RepoRoot "tmp\zenodo-public-readback-$RecordId"
$tempZip = Join-Path $tempRoot "remote.zip"
$outputDirectory = Split-Path -Parent $OutputPrefix

New-Item -ItemType Directory -Force -Path $tempRoot, $outputDirectory | Out-Null

function Get-Sha256 {
  param([Parameter(Mandatory)][string]$Path)
  return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToUpperInvariant()
}

function Get-StreamSha256 {
  param([Parameter(Mandatory)][System.IO.Stream]$Stream)
  $sha = [System.Security.Cryptography.SHA256]::Create()
  try {
    return ([Convert]::ToHexString($sha.ComputeHash($Stream))).ToUpperInvariant()
  }
  finally {
    $sha.Dispose()
  }
}

function Test-UnsafeZipName {
  param([Parameter(Mandatory)][string]$Name)
  $normalized = $Name.Replace("\", "/")
  if ($normalized.StartsWith("/") -or $normalized -match "^[A-Za-z]:") {
    return $true
  }
  return @($normalized.Split("/") | Where-Object { $_ -eq ".." }).Count -gt 0
}

function Get-ZipInventory {
  param([Parameter(Mandatory)][string]$Path)
  $archive = [System.IO.Compression.ZipFile]::OpenRead($Path)
  try {
    $members = [System.Collections.Generic.List[object]]::new()
    $unsafe = [System.Collections.Generic.List[string]]::new()
    $uncompressedBytes = [int64]0
    foreach ($entry in $archive.Entries) {
      $relativePath = $entry.FullName.Replace("\", "/")
      $isDirectory = [string]::IsNullOrEmpty($entry.Name)
      if (Test-UnsafeZipName -Name $relativePath) {
        $unsafe.Add($relativePath)
      }
      if ($isDirectory) {
        $members.Add([ordered]@{
          relative_path = $relativePath
          is_directory = $true
          bytes = 0
          sha256 = $null
        })
        continue
      }
      $stream = $entry.Open()
      try {
        $sha256 = Get-StreamSha256 -Stream $stream
      }
      finally {
        $stream.Dispose()
      }
      $uncompressedBytes += [int64]$entry.Length
      $members.Add([ordered]@{
        relative_path = $relativePath
        is_directory = $false
        bytes = [int64]$entry.Length
        sha256 = $sha256
      })
    }
    return [ordered]@{
      file_members = @($members | Where-Object { -not $_.is_directory }).Count
      all_entries = $members.Count
      uncompressed_bytes = $uncompressedBytes
      unsafe_names = @($unsafe)
      crc_error = $null
      members = @($members | Sort-Object relative_path)
    }
  }
  catch {
    return [ordered]@{
      file_members = 0
      all_entries = 0
      uncompressed_bytes = 0
      unsafe_names = @()
      crc_error = $_.Exception.Message
      members = @()
    }
  }
  finally {
    $archive.Dispose()
  }
}

function Convert-MembersToMap {
  param([Parameter(Mandatory)][object[]]$Members)
  $map = @{}
  foreach ($member in $Members) {
    $map[[string]$member.relative_path] = $member
  }
  return $map
}

function Compare-ZipInventories {
  param(
    [Parameter(Mandatory)][string]$ZipName,
    [Parameter(Mandatory)]$Expected,
    [Parameter(Mandatory)]$Actual,
    [Parameter(Mandatory)][AllowEmptyCollection()][System.Collections.Generic.List[string]]$Errors
  )
  foreach ($field in @("file_members", "all_entries", "uncompressed_bytes")) {
    if ([int64]$Expected.$field -ne [int64]$Actual.$field) {
      $Errors.Add("$ZipName ${field}: expected $($Expected.$field), got $($Actual.$field)")
    }
  }
  if (@($Actual.unsafe_names).Count -ne 0) {
    $Errors.Add("$ZipName has unsafe names: $(@($Actual.unsafe_names) -join ', ')")
  }
  if ($null -ne $Actual.crc_error) {
    $Errors.Add("$ZipName ZIP read error: $($Actual.crc_error)")
  }

  $expectedMap = Convert-MembersToMap -Members @($Expected.members)
  $actualMap = Convert-MembersToMap -Members @($Actual.members)
  foreach ($path in $expectedMap.Keys) {
    if (-not $actualMap.ContainsKey($path)) {
      $Errors.Add("$ZipName missing member: $path")
      continue
    }
    $expectedMember = $expectedMap[$path]
    $actualMember = $actualMap[$path]
    if ([bool]$expectedMember.is_directory -ne [bool]$actualMember.is_directory) {
      $Errors.Add("$ZipName member kind mismatch: $path")
    }
    if ([int64]$expectedMember.bytes -ne [int64]$actualMember.bytes) {
      $Errors.Add("$ZipName member byte mismatch: $path")
    }
    if (-not [bool]$expectedMember.is_directory -and
        ([string]$expectedMember.sha256).ToUpperInvariant() -ne ([string]$actualMember.sha256).ToUpperInvariant()) {
      $Errors.Add("$ZipName member SHA-256 mismatch: $path")
    }
  }
  foreach ($path in $actualMap.Keys) {
    if (-not $expectedMap.ContainsKey($path)) {
      $Errors.Add("$ZipName unexpected member: $path")
    }
  }
}

function Invoke-Download {
  param(
    [Parameter(Mandatory)][System.Net.Http.HttpClient]$Client,
    [Parameter(Mandatory)][string]$Url,
    [Parameter(Mandatory)][string]$Path
  )
  $lastError = $null
  for ($attempt = 1; $attempt -le 5; $attempt++) {
    try {
      if (Test-Path -LiteralPath $Path) {
        Remove-Item -LiteralPath $Path -Force
      }
      $response = $Client.GetAsync($Url, [System.Net.Http.HttpCompletionOption]::ResponseHeadersRead).GetAwaiter().GetResult()
      try {
        $response.EnsureSuccessStatusCode() | Out-Null
        $inputStream = $response.Content.ReadAsStream()
        try {
          $outputStream = [System.IO.File]::Open($Path, [System.IO.FileMode]::CreateNew, [System.IO.FileAccess]::Write, [System.IO.FileShare]::None)
          try {
            $inputStream.CopyTo($outputStream)
          }
          finally {
            $outputStream.Dispose()
          }
        }
        finally {
          $inputStream.Dispose()
        }
      }
      finally {
        $response.Dispose()
      }
      return
    }
    catch {
      $lastError = $_
      if ($attempt -lt 5) {
        Start-Sleep -Seconds ([Math]::Min(20, [Math]::Pow(2, $attempt)))
      }
    }
  }
  throw $lastError
}

function Get-RemoteSha256 {
  param(
    [Parameter(Mandatory)][System.Net.Http.HttpClient]$Client,
    [Parameter(Mandatory)][string]$Url
  )
  $lastError = $null
  for ($attempt = 1; $attempt -le 5; $attempt++) {
    try {
      $response = $Client.GetAsync($Url, [System.Net.Http.HttpCompletionOption]::ResponseHeadersRead).GetAwaiter().GetResult()
      try {
        $response.EnsureSuccessStatusCode() | Out-Null
        $stream = $response.Content.ReadAsStream()
        try {
          return Get-StreamSha256 -Stream $stream
        }
        finally {
          $stream.Dispose()
        }
      }
      finally {
        $response.Dispose()
      }
    }
    catch {
      $lastError = $_
      if ($attempt -lt 5) {
        Start-Sleep -Seconds ([Math]::Min(20, [Math]::Pow(2, $attempt)))
      }
    }
  }
  throw $lastError
}

foreach ($requiredPath in @($ExpectedManifestPath, $ExpectedValidationPath, $PredecessorZipReadbackPath, $NewZipPath)) {
  if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
    throw "Required input is missing: $requiredPath"
  }
}

$expectedFiles = [ordered]@{}
foreach ($row in (Import-Csv -LiteralPath $ExpectedManifestPath)) {
  $expectedFiles[$row.filename] = [ordered]@{
    bytes = [int64]$row.bytes
    sha256 = ([string]$row.sha256).ToUpperInvariant()
  }
}
$expectedFiles[$manifestName] = [ordered]@{
  bytes = [int64](Get-Item -LiteralPath $ExpectedManifestPath).Length
  sha256 = Get-Sha256 -Path $ExpectedManifestPath
}
$expectedFiles[$validationName] = [ordered]@{
  bytes = [int64](Get-Item -LiteralPath $ExpectedValidationPath).Length
  sha256 = Get-Sha256 -Path $ExpectedValidationPath
}

$predecessorZipReadback = Get-Content -Raw -LiteralPath $PredecessorZipReadbackPath | ConvertFrom-Json
$expectedNewZip = Get-ZipInventory -Path $NewZipPath
if ($null -ne $expectedNewZip.crc_error) {
  throw "Local new ZIP could not be read: $($expectedNewZip.crc_error)"
}

$client = [System.Net.Http.HttpClient]::new()
$client.Timeout = [TimeSpan]::FromMinutes(20)
$client.DefaultRequestHeaders.UserAgent.ParseAdd("modern-latex-manuscripts-public-readback/20260723")
$errors = [System.Collections.Generic.List[string]]::new()
$outerReadback = [ordered]@{}
$zipReadback = [ordered]@{}

try {
  $apiResponse = $client.GetStringAsync($apiUrl).GetAwaiter().GetResult()
  $api = $apiResponse | ConvertFrom-Json
  $apiResponse | Set-Content -LiteralPath "$OutputPrefix.json" -Encoding utf8NoBOM

  if ([int64]$api.id -ne $RecordId) {
    $errors.Add("API record ID mismatch: expected $RecordId, got $($api.id)")
  }
  if ([string]$api.conceptdoi -ne "10.5281/zenodo.20410947") {
    $errors.Add("Concept DOI mismatch: $($api.conceptdoi)")
  }

  $remoteFiles = @{}
  foreach ($file in $api.files) {
    $remoteFiles[[string]$file.key] = $file
  }
  foreach ($filename in $expectedFiles.Keys) {
    if (-not $remoteFiles.ContainsKey($filename)) {
      $errors.Add("Missing public file: $filename")
    }
  }
  foreach ($filename in $remoteFiles.Keys) {
    if (-not $expectedFiles.Contains($filename)) {
      $errors.Add("Unexpected public file: $filename")
    }
  }

  foreach ($filename in @($remoteFiles.Keys | Sort-Object)) {
    if (-not $expectedFiles.Contains($filename)) {
      continue
    }
    $remote = $remoteFiles[$filename]
    $expected = $expectedFiles[$filename]
    $url = [string]$remote.links.self
    if ([int64]$remote.size -ne [int64]$expected.bytes) {
      $errors.Add("$filename API byte mismatch: expected $($expected.bytes), got $($remote.size)")
    }

    if ($filename.EndsWith(".zip", [StringComparison]::OrdinalIgnoreCase)) {
      Invoke-Download -Client $client -Url $url -Path $tempZip
      $actualBytes = [int64](Get-Item -LiteralPath $tempZip).Length
      $actualSha256 = Get-Sha256 -Path $tempZip
      $actualZip = Get-ZipInventory -Path $tempZip
      if ($filename -eq $newZipName) {
        $expectedZip = $expectedNewZip
      }
      else {
        $property = $predecessorZipReadback.PSObject.Properties[$filename]
        if ($null -eq $property) {
          $errors.Add("No predecessor member ledger for retained ZIP: $filename")
          $expectedZip = $null
        }
        else {
          $expectedZip = $property.Value
        }
      }
      if ($null -ne $expectedZip) {
        Compare-ZipInventories -ZipName $filename -Expected $expectedZip -Actual $actualZip -Errors $errors
      }
      $zipReadback[$filename] = $actualZip
      Remove-Item -LiteralPath $tempZip -Force
    }
    else {
      $actualBytes = [int64]$remote.size
      $actualSha256 = Get-RemoteSha256 -Client $client -Url $url
    }

    if ($actualBytes -ne [int64]$expected.bytes) {
      $errors.Add("$filename downloaded byte mismatch: expected $($expected.bytes), got $actualBytes")
    }
    if ($actualSha256 -ne [string]$expected.sha256) {
      $errors.Add("$filename SHA-256 mismatch: expected $($expected.sha256), got $actualSha256")
    }
    $outerReadback[$filename] = [ordered]@{
      bytes = $actualBytes
      sha256 = $actualSha256
      url = $url
    }
  }
}
finally {
  $client.Dispose()
  if (Test-Path -LiteralPath $tempZip) {
    Remove-Item -LiteralPath $tempZip -Force
  }
}

$outerReadback | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath "${OutputPrefix}_public_readback.json" -Encoding utf8NoBOM
$zipReadback | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath "${OutputPrefix}_zip_member_readback.json" -Encoding utf8NoBOM

$zipFileMembers = [int64]0
$zipUncompressedBytes = [int64]0
foreach ($zip in $zipReadback.Values) {
  $zipFileMembers += [int64]$zip.file_members
  $zipUncompressedBytes += [int64]$zip.uncompressed_bytes
}
$outerBytes = [int64]0
foreach ($file in $outerReadback.Values) {
  $outerBytes += [int64]$file.bytes
}

$result = [ordered]@{
  status = if ($errors.Count -eq 0) { "PASS" } else { "FAIL" }
  errors = @($errors)
  record_id = $RecordId
  doi = "10.5281/zenodo.$RecordId"
  concept_doi = "10.5281/zenodo.20410947"
  expected_files = $expectedFiles.Count
  public_files = $outerReadback.Count
  public_bytes = $outerBytes
  zip_archives = $zipReadback.Count
  zip_file_members = $zipFileMembers
  zip_uncompressed_bytes = $zipUncompressedBytes
  outer_readback_path = "${OutputPrefix}_public_readback.json"
  zip_readback_path = "${OutputPrefix}_zip_member_readback.json"
}
$result | ConvertTo-Json -Depth 8
if ($errors.Count -ne 0) {
  exit 1
}
