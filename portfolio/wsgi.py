"""
wsgi.py – Fixed for Vercel (2025 working version)
"""

import os
from django.core.wsgi import get_wsgi_application

# This line is REQUIRED for Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# This variable name MUST be "application" (Vercel looks for it)
application = get_wsgi_application()