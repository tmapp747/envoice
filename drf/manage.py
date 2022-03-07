#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.conf import settings


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    ## if in DEBUG and server is running (autoreload enabled)
    if settings.DEBUG:
        if os.environ.get('RUN_MAIN'): 
            import debugpy
            # start debugger
            debugpy.listen(('0.0.0.0',3000))
            # catch the run debug event
            debugpy.wait_for_client()
            print('[DEBUG] Debugging ready to start...')
    ###

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
