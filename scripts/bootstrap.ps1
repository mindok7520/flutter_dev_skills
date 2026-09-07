param(
    [Parameter(Mandatory = $true)][string]$Target,
    [switch]$Apply,
    [switch]$WithTooling,
    [switch]$WithCi,
    [switch]$OnlyTooling
)
$ErrorActionPreference = 'Stop'
$installArguments = @((Join-Path $PSScriptRoot 'install.py'), '--target', $Target)
if ($Apply) { $installArguments += '--apply' }
if ($WithTooling) { $installArguments += '--with-tooling' }
if ($WithCi) { $installArguments += '--with-ci' }
if ($OnlyTooling) { $installArguments += '--only-tooling' }
& python @installArguments
exit $LASTEXITCODE
