from django.urls import path

from config import settings
from .views import home, create_article_view \
   , articles_view, article_view, user_articles_view, update_article_view, delete_article_view

urlpatterns = [
   path('',home,name='home'),
   path('create_article/<str:slug>-<int:pk>',create_article_view,name='create_article'),
   path('article/<str:slug>',article_view,name='article'),
   path('article/update/<str:slug>',update_article_view,name='update_article'),
   path('articles/<str:slug>',user_articles_view,name='user_articles'),
   path('article/delete/<str:slug>',delete_article_view,name='delete_article'),
   path('articles/',articles_view,name='articles'),

]