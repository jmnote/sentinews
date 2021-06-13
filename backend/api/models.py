from django.db import models

# Create your models here.

class Article(models.Model):
    url = models.CharField(max_length=80)
    user_ip = models.CharField(max_length=16)
    status = models.CharField(max_length=16)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200, null=True, blank=True, default=None) 
    content = models.CharField(max_length=10000, null=True, blank=True, default=None)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
