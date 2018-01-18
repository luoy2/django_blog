#现在你的views.py应该是这样
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Article
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from datetime import datetime
# Create your views here.
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})


def detail(request, pk):
    try:
        post = Article.objects.get(id=str(pk))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})


# class DetailView(generic.DeleteView):
#     model = Article
#     template_name = 'article_detail.html'

# def test(request) :
#     return render(request, 'test.html', {'current_time': datetime.now()})