from django.contrib import admin

# Register your models here.
from .models import Article


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']


# class ChoiceInLine(admin.StackedInline):
#     model = Choice
#     extra = 3


class ArticleInLine(admin.TabularInline):
    model = Article
    extra = 3


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    list_display = ('title', 'pub_date', 'category')
    search_fields = ['content']
    fieldsets = [
        ('Title', {'fields':['title']}),
        ('Content', {'fields':['content', 'category']}),
    ]
    # inlines = [ArticleInLine]




admin.site.register(Article, ArticleAdmin)
