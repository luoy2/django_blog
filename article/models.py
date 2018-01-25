from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown

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
    tags = models.ManyToManyField(Tag, blank=True, max_length=99999999999999)
    content = models.TextField(blank=True, null=True)
    excerpt = models.TextField(blank=True)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'pk': self.pk})

    def increase_view(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(['extra','codehilite'])
            self.excerpt = strip_tags(md.convert(self.content))[:54]
        super(Article, self).save(*args, **kwargs)

    class Meta:  # 按时间下降排序
        ordering = ['-pub_date']



