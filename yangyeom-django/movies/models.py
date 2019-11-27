from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    code = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    watched_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Review', related_name='watched_movies')
    score_exp_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ScoresExpected', related_name='score_exp_movies')
    score_avg = models.IntegerField(default=0)

class Review(models.Model):
    content = models.CharField(max_length=100, blank=True)
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ScoresExpected(models.Model):
    score = models.FloatField(default=0)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)