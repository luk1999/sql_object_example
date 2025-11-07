from pathlib import Path

BASE_APP_DIR = Path(__file__).parent.parent

DATABASE_FILE_PATH = str(BASE_APP_DIR / "db.sqlite")
DATABASE_CONNECTION_STR = f"sqlite:{DATABASE_FILE_PATH}"
