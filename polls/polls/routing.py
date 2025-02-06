from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/polls/<str:poll_id>/', consumers.PollConsumer.as_asgi()),
]
