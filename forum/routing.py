from channels.routing import route

channel_routing=[route('websocket.receive',chat.consumers.ws_echo),
route('websoket.connect','chat.consumers.ws_add',path=r"^/chat/(?P<room>\w+)$")]