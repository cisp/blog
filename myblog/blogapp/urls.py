from django.urls import path
from . import views

urlpatterns = [
    path('index', views.blog_title, name="blog_title"),
    path('<int:blogid>', views.blog_content, name="blog_content"),
]
