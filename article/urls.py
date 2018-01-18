from django.urls import path
from . import views

app_name = 'article'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path(r'archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path(r'categories/<int:pk>/', views.category, name='category')
]