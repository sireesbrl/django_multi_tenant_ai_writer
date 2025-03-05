import environ
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = BASE_DIR / "features"
