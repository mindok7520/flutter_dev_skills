param(
    [Parameter(Mandatory = $true)][string]$Target,
    [switch]$Apply,
    [switch]$WithTooling,
    [switch]$WithCi
)
$ErrorActionPreference = 'Stop'
$installArguments = @((Join-Path $PSScriptRoot 'install.py'), '--target', $Target)
if ($Apply) { $installArguments += '--apply' }
if ($WithTooling) { $installArguments += '--with-tooling' }
if ($WithCi) { $installArguments += '--with-ci' }
& python @installArguments
exit $LASTEXITCODE
