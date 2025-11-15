#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

# Ensure the project root (parent of the outer project dir) is on sys.path so
# sibling apps (like the top-level `dashboard` package) can be imported when
# running manage.py from the `projeto` directory.
# Example: if manage.py is at <root>/projeto/manage.py and apps live at
# <root>/dashboard, we need <root> on sys.path.
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
