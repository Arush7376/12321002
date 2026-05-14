import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application


REPO_ROOT = Path(__file__).resolve().parents[3]
SERVICE_SRC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SERVICE_SRC))
sys.path.insert(0, str(REPO_ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
