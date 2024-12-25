from rest_framework.viewsets import ModelViewSet
from .models import Idea, Team, UserProfile
from .serializers import IdeaSerializer, TeamSerializer, UserProfileSerializer

class IdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
