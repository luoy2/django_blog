from ..models import *
from django import template
from django.db.models.aggregates import Count


register=template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Article.objects.all().order_by('-pub_date')[:num]

@register.simple_tag
def archives():
    return Article.objects.dates('pub_date', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_categories():
    return Category.objects.all()