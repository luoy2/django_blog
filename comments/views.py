from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article

from .models import Comments
from .forms import CommentForm
