from django.urls import path, include

from .views import UserViewSet, PublicationViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('videos', PublicationViewSet)

urlpatterns = [
    path('router/', include(router.urls)),

]
