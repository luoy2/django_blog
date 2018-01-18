from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length= 100)
    def __str__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(default=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField(blank=True, null=True)
    excerpt = models.TextField(blank=True)
    def __str__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']




