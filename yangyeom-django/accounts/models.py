from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)
    similar_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reference_users', through='Similarity', blank=True)
    # score_total = models.FloatField(default=0)
    score_avg = models.FloatField(default=0)
    paid = models.BooleanField(default=False)

class Similarity(models.Model):
    # 여기서 related_name이 필요한 이유: similarity 값으로 역참조해서 찾을 때 쓰임. 근데 그럴 일 없으니까 아무 이름이나 써도 됨!
    reference_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="a", on_delete=models.CASCADE)
    similar_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="b", on_delete=models.CASCADE)
    similarity = models.FloatField(default=0)
