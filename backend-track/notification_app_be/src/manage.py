#!/usr/bin/env python
import os
import sys
from pathlib import Path


def main():
    src_dir = Path(__file__).resolve().parent
    repo_root = src_dir.parents[1]
    sys.path.insert(0, str(src_dir))
    sys.path.insert(0, str(repo_root))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
