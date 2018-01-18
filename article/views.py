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
    post = get_object_or_404(Article, pk=pk)
    return render(request, 'detail.html', {'post' : post})


def index(request):
    article_lsit = Article.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'post_list':article_lsit})

class DetailView(generic.DeleteView):
    model = Article
    template_name = 'detail.html'

# def test(request) :
#     return render(request, 'test.html', {'current_time': datetime.now()})