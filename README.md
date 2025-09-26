# calc-cli

A robust command-line calculator with a REPL, full unit tests, and CI that enforces **100% coverage**.

## Features
- REPL: `help`, `quit`, and arithmetic commands (`+ - * /` or `add sub mul div`)
- Clear prompts, validation, and graceful error handling
- DRY, modular design: parsing, operations, and REPL separated
- Pytest suite (including parameterized tests)
- GitHub Actions workflow fails if coverage < 100%

## Quickstart

### 1) Create and activate virtual environment
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
