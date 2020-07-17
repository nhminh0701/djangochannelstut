from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing


application = ProtocolTypeRouter({
    #(http->django views added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.urlpatterns,
        )
    )
})