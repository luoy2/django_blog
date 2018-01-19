from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article

from .models import Comments
from .forms import CommentForm

def post_comment(request, post_pk):
    article = get_object_or_404(Article, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article)
        else:
            comment_list = article.comment_set.all()
            context = {'post':article,
                       'form':form,
                       'comment_list':comment_list}
            return render(request, 'detail.html', context=context)
    return redirect(article)