from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[
        ('mentor', 'Mentor'),
        ('student', 'Student'),
        ('initiator', 'Initiator'),
    ])