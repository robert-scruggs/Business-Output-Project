"""
WSGI config for BRO project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BRO.settings")

application = get_wsgi_application()

# Get the path of the current file (WSGI configuration file)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path of the project directory (assuming the BRO module is in the project root)
project_dir = os.path.dirname(current_dir)

# Add the project directory to sys.path
sys.path.append(project_dir)

