from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import TokenAuthConsumer, ChatConsumer, NotificacionConsumer

application = ProtocolTypeRouter({
    # HTTP protocol
    'http': URLRouter([]),

    # WebSocket protocol
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/token-auth/', TokenAuthConsumer.as_asgi()),
            path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
            path('ws/notificaciones/', NotificacionConsumer.as_asgi()),
        ])
    ),
})
