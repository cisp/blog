from django.shortcuts import render
from .models import BlogArticles
# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blogs/titles.html", {"blogs":blogs})

def blog_content(request,blogid):
    article = BlogArticles.objects.get(id=blogid)
    pub = article.publish
    return render(request, "blogs/content.html", {"article":article, "publish":pub})
