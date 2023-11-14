from django.shortcuts import render
from .models import Blogs


def home(request):
    blogs = Blogs.objects.all()
    return render(request, 'blogs/home.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)
    return render(request, 'blogs/single_blog.html', {'blog': blog})
