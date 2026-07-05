from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DIRECTORIES = [
    "app",
    "app/auth",
    "app/dashboard",
    "app/clients",
    "app/projects",
    "app/records",
    "app/hr",
    "app/finance",
    "app/training",
    "app/mel",
    "app/integrations",
    "app/reports",
    "app/models",
    "app/services",
    "app/utils",
    "app/static/css",
    "app/static/js",
    "app/static/img",
    "app/static/icons",
    "app/templates",
    "config",
    "docs",
    "migrations",
    "tests",
    "uploads",
    "backups",
    "instance",
    ".vscode"
]

INIT_PACKAGES = [
    "app",
    "app/auth",
    "app/dashboard",
    "app/clients",
    "app/projects",
    "app/records",
    "app/hr",
    "app/finance",
    "app/training",
    "app/mel",
    "app/integrations",
    "app/reports",
    "app/models",
    "app/services",
    "app/utils"
]

FILES = {
    "README.md": "# CDCS Digital Operations Platform (CDCS-DOP)\n",
    ".env.example": (
        "FLASK_APP=run.py\n"
        "FLASK_ENV=development\n"
        "SECRET_KEY=change-me\n"
        "DATABASE_URL=sqlite:///instance/cdcs.db\n"
    ),
    ".gitignore": (
        "venv/\n"
        "__pycache__/\n"
        "*.pyc\n"
        ".env\n"
        "instance/\n"
        "uploads/\n"
        "backups/\n"
    )
}


def ensure_directory(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    print(f"[OK] Directory: {path.relative_to(PROJECT_ROOT)}")


def ensure_file(path: Path, content: str = ""):
    if not path.exists():
        path.write_text(content, encoding="utf-8")
        print(f"[OK] File: {path.relative_to(PROJECT_ROOT)}")
    else:
        print(f"[SKIP] File exists: {path.relative_to(PROJECT_ROOT)}")


def main():
    print("\nCDCS-DOP Bootstrap\n")

    for directory in DIRECTORIES:
        ensure_directory(PROJECT_ROOT / directory)

    for package in INIT_PACKAGES:
        ensure_file(PROJECT_ROOT / package / "__init__.py")

    for filename, content in FILES.items():
        ensure_file(PROJECT_ROOT / filename, content)

    print("\nBootstrap completed successfully.")


if __name__ == "__main__":
    main()