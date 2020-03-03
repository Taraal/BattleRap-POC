from django.urls import path, include

from .views import UserViewSet, VideoViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('videos', VideoViewSet)

urlpatterns = [
    path('router/', include(router.urls)),
]
