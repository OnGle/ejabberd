import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../speeqeweb')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "speeqeweb.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
