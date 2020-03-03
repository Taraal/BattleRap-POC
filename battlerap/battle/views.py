from django.core import serializers
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from rest_framework.response import Response


from .models import User, Publication, Vote
from .serializers import UserSerializer, PublicationSerializer, VoteSerializer
from .utils import get_timedelta


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PublicationViewSet(viewsets.GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    @action(methods=['get'], url_path='trending', url_name='trending')
    def get_trending(self, request):
        last_week = get_timedelta(7)
        pub_list = Publication.objects.filter(date__lt=last_week).order_by('votes')

        serializer = self.get_serializer(pub_list, many=True)
        return Response(serializer.data)

    @action(methods=['get'], url_path='compare', url_name='compare')
    def compare(self, first_pub, second_pub):
        time = get_timedelta(1)
        votes_fp = Vote.objects.filter(publication__id=first_pub, date__lt=time).count()
        votes_sp = Vote.objects.filter(publication__id=second_pub, date__lt=time).count()
        answer = {
            first_pub: votes_fp,
            second_pub: votes_sp
        }
        answer_json = serializers.serialize('json', answer)
        return Response(data=answer_json)


class VoteViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


