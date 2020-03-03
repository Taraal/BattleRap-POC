from django.db import models

# Create your models here.


class User(models.Model):
    username = models.TextField(null=True)
    password = models.TextField(null=True)
    victoires = models.IntegerField(null=True, default=0)
    participation = models.IntegerField(null=True, default=0)
    top_two = models.IntegerField(null=True, default=0)
    top_three = models.IntegerField(null=True, default=0)
    description = models.TextField(null=True)


class Video(models.Model):
    description = models.TextField(null=True)
    video = models.TextField(null=True)
    user = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)


class Tags(models.Model):
    videos = models.ManyToManyField(Video)


class Tournois(models.Model):
    user = models.ForeignKey(User, related_name='tournois', on_delete=models.CASCADE)
    rank = models.IntegerField(null=True, default=32)
