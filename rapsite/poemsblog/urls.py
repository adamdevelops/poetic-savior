from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<int:pk>',views.blog_detail, name='detail')
]
