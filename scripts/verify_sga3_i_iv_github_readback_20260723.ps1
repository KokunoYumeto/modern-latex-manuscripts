[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Commit,

    [Parameter(Mandatory = $true)]
    [string]$PackageRoot,

    [Parameter(Mandatory = $true)]
    [string]$PackageRelativePath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath
)

$ErrorActionPreference = 'Stop'

function Get-StreamSha256 {
    param([Parameter(Mandatory = $true)][System.IO.Stream]$Stream)

    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        ([BitConverter]::ToString($sha.ComputeHash($Stream))).Replace('-', '')
    }
    finally {
        $sha.Dispose()
    }
}

function Read-ZipEntryText {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.Compression.ZipArchiveEntry]$Entry
    )

    $stream = $Entry.Open()
    try {
        $reader = [System.IO.StreamReader]::new(
            $stream,
            [System.Text.UTF8Encoding]::new($false, $true),
            $true,
            4096,
            $false
        )
        try {
            $reader.ReadToEnd()
        }
        finally {
            $reader.Dispose()
        }
    }
    finally {
        $stream.Dispose()
    }
}

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$root = (Resolve-Path -LiteralPath $PackageRoot).Path
$files = @(Get-ChildItem -LiteralPath $root -File | Sort-Object Name)
if ($files.Count -ne 6) {
    throw "Expected six package files, found $($files.Count)."
}

$tempRoot = Join-Path $env:TEMP (
    'sga3-i-iv-github-readback-' + [Guid]::NewGuid().ToString('N')
)
New-Item -ItemType Directory -Path $tempRoot | Out-Null
try {
    $outer = [ordered]@{}
    foreach ($file in $files) {
        $url = (
            'https://raw.githubusercontent.com/' +
            'KokunoYumeto/modern-latex-manuscripts/' +
            $Commit + '/' + $PackageRelativePath + '/' + $file.Name
        )
        $destination = Join-Path $tempRoot $file.Name
        Invoke-WebRequest `
            -UseBasicParsing `
            -Uri $url `
            -OutFile $destination

        $localHash = (
            Get-FileHash -Algorithm SHA256 -LiteralPath $file.FullName
        ).Hash
        $remoteHash = (
            Get-FileHash -Algorithm SHA256 -LiteralPath $destination
        ).Hash
        $remoteBytes = (Get-Item -LiteralPath $destination).Length
        if ($remoteBytes -ne $file.Length -or $remoteHash -ne $localHash) {
            throw "GitHub outer-file mismatch: $($file.Name)"
        }
        $outer[$file.Name] = [ordered]@{
            bytes = [int64]$file.Length
            sha256 = $remoteHash
            url = $url
        }
    }

    $zipName = (
        'SGA3_English_Through_Expose_IV_Loop2_ReferenceV2_R2_' +
        'Source_Ledgers_20260723.zip'
    )
    $archive = [System.IO.Compression.ZipFile]::OpenRead(
        (Join-Path $tempRoot $zipName)
    )
    try {
        $entries = @(
            $archive.Entries |
                Where-Object { -not [string]::IsNullOrEmpty($_.Name) } |
                Sort-Object FullName
        )
        if ($entries.Count -ne 199) {
            throw "Expected 199 ZIP members, found $($entries.Count)."
        }
        $zipUncompressedBytes = [int64](
            $entries | Measure-Object -Property Length -Sum
        ).Sum
        if ($zipUncompressedBytes -ne 6911184) {
            throw "Unexpected ZIP uncompressed bytes: $zipUncompressedBytes"
        }

        $manifestEntry = @(
            $entries | Where-Object { $_.FullName -eq 'SHA256SUMS.csv' }
        )
        if ($manifestEntry.Count -ne 1) {
            throw "Expected one inner manifest, found $($manifestEntry.Count)."
        }
        $innerRows = @(
            (Read-ZipEntryText -Entry $manifestEntry[0]) |
                ConvertFrom-Csv
        )
        if ($innerRows.Count -ne 198) {
            throw "Expected 198 inner rows, found $($innerRows.Count)."
        }
        $innerByPath = @{}
        foreach ($row in $innerRows) {
            $innerByPath[$row.relative_path] = $row
        }

        $members = foreach ($entry in $entries) {
            $stream = $entry.Open()
            try {
                $hash = Get-StreamSha256 -Stream $stream
            }
            finally {
                $stream.Dispose()
            }

            if ($entry.FullName -eq 'SHA256SUMS.csv') {
                $expectedHash = (
                    '2F78F112B9F5A368725E56AD432B13EAE9B8EE08052AC3B699C0A22452EE6DC8'
                )
            }
            else {
                $row = $innerByPath[$entry.FullName]
                if ($null -eq $row) {
                    throw "Unmanifested ZIP member: $($entry.FullName)"
                }
                if ($entry.Length -ne [int64]$row.bytes) {
                    throw "ZIP member byte mismatch: $($entry.FullName)"
                }
                $expectedHash = $row.sha256
            }
            if ($hash -ne $expectedHash) {
                throw "ZIP member hash mismatch: $($entry.FullName)"
            }

            [ordered]@{
                relative_path = $entry.FullName
                bytes = [int64]$entry.Length
                sha256 = $hash
            }
        }
    }
    finally {
        $archive.Dispose()
    }

    $receipt = [ordered]@{
        status = 'PASS'
        errors = @()
        repository = 'KokunoYumeto/modern-latex-manuscripts'
        commit = $Commit
        package_path = $PackageRelativePath
        outer_files = $outer.Count
        outer_readback = $outer
        zip = [ordered]@{
            name = $zipName
            file_members = $members.Count
            uncompressed_bytes = $zipUncompressedBytes
            members = @($members)
        }
    }
    $receiptText = ($receipt | ConvertTo-Json -Depth 12) + "`n"
    [System.IO.File]::WriteAllText(
        $OutputPath,
        $receiptText,
        [System.Text.UTF8Encoding]::new($false)
    )

    [pscustomobject]@{
        status = 'PASS'
        commit = $Commit
        outer_files = $outer.Count
        zip_members = $members.Count
        zip_uncompressed_bytes = $zipUncompressedBytes
        receipt = $OutputPath
    }
}
finally {
    if (Test-Path -LiteralPath $tempRoot) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}
