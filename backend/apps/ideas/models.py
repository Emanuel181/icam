from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[
        ('mentor', 'Mentor'),
        ('student', 'Student'),
        ('initiator', 'Initiator')
    ])

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    initiator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=100)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    members = models.ManyToManyField(UserProfile)
