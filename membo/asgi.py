"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application
import channels.asgi 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "membo.settings")
# django.setup()
# application = get_default_application()
channel_layer = channels.asgi.get_channel_layer()