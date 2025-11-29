# This file runs during Vercel build to collect static files
import os
from django.conf import settings
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
import django
django.setup()

call_command('collectstatic', '--noinput', verbosity=0)