# LinkedIn Job Searcher - Development Commands
# PowerShell equivalent of Makefile for Windows

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "LinkedIn Job Searcher - Development Commands" -ForegroundColor Cyan
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  help          Show this help message"
    Write-Host "  install       Install production dependencies"
    Write-Host "  install-dev   Install development dependencies"
    Write-Host "  test          Run tests with pytest"
    Write-Host "  test-cov      Run tests with coverage"
    Write-Host "  lint          Run linting checks"
    Write-Host "  format        Format code"
    Write-Host "  check         Run all checks (lint + test)"
    Write-Host "  clean         Clean up build artifacts"
    Write-Host "  run           Run the web application"
    Write-Host "  run-cli       Show CLI help"
    Write-Host "  build         Build distribution packages"
    Write-Host "  release       Prepare for release"
    Write-Host ""
    Write-Host "Usage: .\make.ps1 <command>" -ForegroundColor Yellow
    Write-Host "Example: .\make.ps1 install-dev" -ForegroundColor Yellow
}

function Install-Prod {
    Write-Host "Installing production dependencies..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m pip install -e .
}

function Install-Dev {
    Write-Host "Installing development dependencies..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m pip install -e ".[dev]"
}

function Run-Tests {
    Write-Host "Running tests with pytest..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m pytest -v
}

function Run-TestsCov {
    Write-Host "Running tests with coverage..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m pytest --cov=linkedin_url_builder --cov-report=html --cov-report=term
}

function Run-Lint {
    Write-Host "Running linting checks..." -ForegroundColor Green
    try {
        & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m ruff check .
        & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m black --check .
        & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m isort --check-only .
        Write-Host "✅ All linting checks passed!" -ForegroundColor Green
    } catch {
        Write-Host "❌ Linting checks failed!" -ForegroundColor Red
        exit 1
    }
}

function Format-Code {
    Write-Host "Formatting code..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m black .
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m isort .
    Write-Host "✅ Code formatted!" -ForegroundColor Green
}

function Run-Check {
    Write-Host "Running all checks..." -ForegroundColor Green
    Run-Lint
    Run-Tests
    Write-Host "✅ All checks passed!" -ForegroundColor Green
}

function Clean-Build {
    Write-Host "Cleaning build artifacts..." -ForegroundColor Green
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue build/
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue dist/
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue *.egg-info/
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue .pytest_cache/
    Remove-Item -Force -ErrorAction SilentlyContinue .coverage
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue htmlcov/
    Get-ChildItem -Recurse -Name __pycache__ | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force -ErrorAction SilentlyContinue
    Write-Host "✅ Cleaned!" -ForegroundColor Green
}

function Run-App {
    Write-Host "Starting web application..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" start_app.py
}

function Run-CLI {
    Write-Host "Showing CLI help..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" cli.py --help
}

function Build-Package {
    Write-Host "Building distribution packages..." -ForegroundColor Green
    & "C:/Users/monster/AppData/Local/Programs/Python/Python313/python.exe" -m build
}

function Prepare-Release {
    Write-Host "Preparing for release..." -ForegroundColor Green
    Clean-Build
    Run-Lint
    Run-Tests
    Build-Package
    Write-Host "✅ Ready for release! Run: twine upload dist/*" -ForegroundColor Cyan
}

# Main command dispatcher
switch ($Command.ToLower()) {
    "help" { Show-Help }
    "install" { Install-Prod }
    "install-dev" { Install-Dev }
    "test" { Run-Tests }
    "test-cov" { Run-TestsCov }
    "lint" { Run-Lint }
    "format" { Format-Code }
    "check" { Run-Check }
    "clean" { Clean-Build }
    "run" { Run-App }
    "run-cli" { Run-CLI }
    "build" { Build-Package }
    "release" { Prepare-Release }
    default { 
        Write-Host "Unknown command: $Command" -ForegroundColor Red
        Show-Help 
    }
}
