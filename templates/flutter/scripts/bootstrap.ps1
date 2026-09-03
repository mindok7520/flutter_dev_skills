$ErrorActionPreference = 'Stop'
Push-Location (Split-Path -Parent $PSScriptRoot)
try {
    & dart run tool/bootstrap.dart
    exit $LASTEXITCODE
}
finally { Pop-Location }
