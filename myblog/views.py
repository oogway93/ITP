from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'myblog/home.html', {'title': 'Home', 'post': posts})


def info(request):
    return render(request, 'myblog/info.html', {'title': 'Info'})
