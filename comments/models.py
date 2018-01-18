from django.db import models
from django import forms

# Create your models here.
class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey('article.Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

