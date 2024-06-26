from django.urls import re_path
from .consumers import ChatConsumer

wsPattern = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]
