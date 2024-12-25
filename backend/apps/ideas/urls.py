from rest_framework.routers import DefaultRouter
from .views import IdeaViewSet, TeamViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('ideas', IdeaViewSet)
router.register('teams', TeamViewSet)
router.register('profiles', UserProfileViewSet)

urlpatterns = router.urls
