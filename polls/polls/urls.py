from django.urls import path
from . import views

urlpatterns = [
    path('<str:poll_id>/', views.poll_view, name='poll'),
]
