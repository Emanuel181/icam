from django.urls import path
from .views import login_view, protected_view, register_view, get_csrf_token, mentor_view, student_view, \
    refresh_token_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('protected/', protected_view, name='protected'),
    path('register/', register_view, name='register'),
    path('mentor/', mentor_view, name='mentor-only'),
    path('student/', student_view, name='student-only'),
    path('csrf-token/', get_csrf_token, name='csrf-token'),
    path('refresh/', refresh_token_view, name='refresh-token'),

]
