from datetime import datetime
from django.db import models
# Create your models here.


class User(models.Model):
    username = models.TextField(null=True)
    password = models.TextField(null=True)
    photo_profil = models.ImageField(null=True)
    victoires = models.IntegerField(null=True, default=0)
    participations = models.IntegerField(null=True, default=0)
    top_two = models.IntegerField(null=True, default=0)
    top_three = models.IntegerField(null=True, default=0)
    description = models.TextField(null=True)
    spotify = models.TextField(null=True)
    deezer = models.TextField(null=True)
    twitter = models.TextField(null=True)
    instagram = models.TextField(null=True)


class Publication(models.Model):
    description = models.TextField(null=True)
    publication = models.TextField(null=True) #URL de l'image/vidéo
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    instrumental = models.TextField(null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)


class Tag(models.Model):
    publication = models.ManyToManyField(Publication)


class Tournoi(models.Model):
    user = models.ForeignKey(User, related_name='tournois', on_delete=models.CASCADE)
    rank = models.IntegerField(null=True, default=32)

class Vote(models.Model):
    user = models.ForeignKey(User)
    publication = models.ForeignKey(Publication, related_name='votes', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        unique_together = (("user", "publication"),)