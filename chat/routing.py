from . import consumers
from django.urls import re_path

urlpatterns = [
    # Similar to url name in JS Websocket
    re_path(r'ws/chat/(?P<roomname>\w+)/$', consumers.ChatConsumer)
]