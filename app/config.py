from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent

# Directories your app needs
TEMPLATES_DIR = APP_DIR / "templates"
EXPORTS_DIR = BASE_DIR / "exports"
STATIC_DIR = APP_DIR / "static"

# Create folders if they don't exist
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
STATIC_DIR.mkdir(parents=True, exist_ok=True)
