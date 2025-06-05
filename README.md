# BLCA Tooling

This repository contains various tools and utilities for the Boulevard Lane Community Association (BLCA).

## Tools Available

### QR Code Generator
Located in the `scripts` directory, this tool allows you to generate QR codes from URLs. This can be useful for creating quick access links for community events, notices, or documents.

#### Usage
```bash
python scripts/generate_qr.py --url <your-url>
```

## Requirements
- Python 3.x
- Required Python packages (listed in requirements.txt)

## Setup

### Setting up a Virtual Environment (Recommended)
1. Create a virtual environment:
```powershell
python -m venv venv
```

2. Activate the virtual environment:
- Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```
- Linux/macOS:
```bash
source venv/bin/activate
```

3. Install Python requirements:
```powershell
pip install -r requirements.txt
```

4. Run the desired script from the scripts directory:
```powershell
python scripts/generate_qr.py --url <your-url>
```

To deactivate the virtual environment when you're done:
```powershell
deactivate
```

Note: The virtual environment directory (venv/) is included in .gitignore and won't be committed to the repository.
