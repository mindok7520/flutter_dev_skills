$ErrorActionPreference = 'Stop'
Push-Location (Split-Path -Parent $PSScriptRoot)
try {
    $validationPython = if (Test-Path -LiteralPath '.venv/Scripts/python.exe') { '.venv/Scripts/python.exe' } else { 'python' }
    & $validationPython scripts/validate.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    & $validationPython -m unittest discover -s tests -v
    exit $LASTEXITCODE
}
finally { Pop-Location }
