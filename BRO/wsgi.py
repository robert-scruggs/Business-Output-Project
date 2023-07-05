"""
WSGI config for BRO project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

# Get the path of the project directory (assuming the BRO module is in the project root)
project_dir = os.path.dirname(os.path.abspath(__file__))

# Add the project directory to sys.path
sys.path.append(project_dir)
sys.path.append('Job Projects/BRO/report/financialStatements')
sys.path.append('Job Projects/BRO/report/financialFlashReports')
# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BRO.settings")

# Get the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


