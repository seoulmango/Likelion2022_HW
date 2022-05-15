from django.shortcuts import render, redirect
from .models import Post
import datetime

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
    })

def create(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('home')

    return render(request, 'create.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    post.visit += 1
    post.save()

    return render(request, 'detail.html', {
        'post': post,
    })

def delete(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    post.delete()
    return redirect('home')

def edit(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    if request.method == 'POST':
        post.update(
            title = request.POST['title'],
            content = request.POST['content'],
            update_date = datetime.datetime.now(),
        )
        return redirect('home')
    return render(request, 'edit.html', {
        'post': post,
        })