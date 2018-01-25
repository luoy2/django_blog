# 现在你的views.py应该是这样
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Article, Category
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
import markdown
from datetime import datetime
from comments.forms import CommentForm
from django.views.generic import *


# Create your views here.
# def home(request):
#     post_list = Article.objects.all()  #获取全部的Article对象
#     return render(request, 'home.html', {'post_list' : post_list})
def archives(request, year, month):
    post_list = Article.objects.filter(pub_date__year=year, pub_date__month=month).order_by('-pub_date')
    return render(request, 'index.html', {'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Article, pk=pk)

    # increase view by 1
    post.increase_view()

    post.content = markdown.markdown(post.content, ['extra', 'codehilite', 'toc'])
    form = CommentForm()
    comment_list = post.comments_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'detail.html', context=context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Article.objects.filter(category=cate).order_by('-pub_date')
    return render(request, 'index.html', context={'post_list': post_list})


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 2


def index(request):
    article_lsit = Article.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'post_list': article_lsit})


class CategoryView(IndexView):
    # model = Article
    # template_name = 'index.html'
    # context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increase_view()
        return response

    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.content = markdown.markdown(post.content, ['extra', 'codehilite', 'toc'])
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comments_set.all()
        context.update({'form': form,
                        'comment_list': comment_list}
                       )
        return context
