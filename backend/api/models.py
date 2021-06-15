from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    url = models.CharField(max_length=80, unique=True)
    title = models.CharField(max_length=200) 
    desc = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)
    user_ip = models.CharField(max_length=32)
    content = models.CharField(max_length=10000)
    comments = models.CharField(max_length=1000)
    comments_count = models.IntegerField()
    polarities = models.CharField(max_length=64)
    avg_polarity = models.FloatField()

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.CharField(max_length=300)
