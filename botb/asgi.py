"""
ASGI config for botb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'botb.settings')

django_asgi_app = get_asgi_application()

import widget.routing

application = ProtocolTypeRouter(
	{
		'http': get_asgi_application(),
		'websocket': AllowedHostsOriginValidator(
			AuthMiddlewareStack(URLRouter(widget.routing.websocket_urlpatterns))
		)
	}
)
