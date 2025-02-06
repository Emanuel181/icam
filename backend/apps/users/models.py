from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = [
    ('mentor', 'Mentor'),
    ('student', 'Student'),
    ('initiator', 'Initiator'),
]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
