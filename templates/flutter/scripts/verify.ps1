$ErrorActionPreference = 'Stop'
Push-Location (Split-Path -Parent $PSScriptRoot)
try {
    & dart run tool/verify.dart
    exit $LASTEXITCODE
}
finally { Pop-Location }
