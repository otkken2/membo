from django.urls import path

from . import consumers


websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/',consumers.ChatConsumer),
]

channel_routing = {
    'websocket.connect': consumers.connect,
    'websocket.receive': consumers.receive,
    'websocket.disconnect': consumers.disconnect ,
}