from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets,mixins

from .models import User, Video
from .serializers import UserSerializer, VideoSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class VideoViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer