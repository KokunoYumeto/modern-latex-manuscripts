$ErrorActionPreference = 'Stop'

$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$manifest = Join-Path $root 'SHA256SUMS.txt'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$members = Get-ChildItem -LiteralPath $root -Recurse -File |
    Where-Object { $_.FullName -ne $manifest } |
    ForEach-Object {
        $relative = $_.FullName.Substring($root.Length + 1).Replace('\', '/')
        [pscustomobject]@{
            Relative = $relative
            Hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
        }
    } |
    Sort-Object Relative

$lines = $members | ForEach-Object { '{0}  {1}' -f $_.Hash, $_.Relative }
[System.IO.File]::WriteAllText($manifest, (($lines -join "`n") + "`n"), $utf8NoBom)

[pscustomobject]@{
    root = $root
    manifest = $manifest
    entries = $members.Count
    manifest_bytes = (Get-Item -LiteralPath $manifest).Length
    manifest_sha256 = (Get-FileHash -LiteralPath $manifest -Algorithm SHA256).Hash
} | ConvertTo-Json
