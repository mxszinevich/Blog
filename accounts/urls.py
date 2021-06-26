from django.urls import path

from config import settings
from .views import  login_view,register_view,logout_view,update_view,personal_cabinet_view

urlpatterns = [
   path('login',login_view,name='login'),
   path('logout',logout_view,name='logout'),
   path('register',register_view,name='register'),
   path('update/<str:slug>-<int:pk>',update_view,name='update'),
   path('personal_cabinet/<str:slug>-<int:pk>',personal_cabinet_view,name='personal_cabinet')
]