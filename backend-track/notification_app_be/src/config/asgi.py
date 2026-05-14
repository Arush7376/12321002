import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application


BASE_DIR = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(BASE_DIR.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings.production")

application = get_asgi_application()
