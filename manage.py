#!/usr/bin/env python
import os
import sys

from avara.boot import fix_path
fix_path()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "avara.settings")

    from djangae.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
