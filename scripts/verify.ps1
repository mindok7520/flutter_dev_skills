$ErrorActionPreference = 'Stop'
Push-Location (Split-Path -Parent $PSScriptRoot)
try {
    & python scripts/validate.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    & python -m unittest discover -s tests -v
    exit $LASTEXITCODE
}
finally { Pop-Location }
