from http.client import FOUND
from django.shortcuts import render, redirect
from .models import Post, Comment
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
    })

@login_required(login_url="/registration/login")
def create(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
        )
        return redirect('home')

    return render(request, 'create.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method == 'POST':
        new_comment = Comment.objects.create(
            post = post,
            content = request.POST['content'],
            author = request.user,
        )
        return redirect('detail', post_pk)

    post.visit += 1
    post.save()
    return render(request, 'detail.html', {
        'post': post,
    })

def delete(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.filter(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def edit(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    if request.method == 'POST':
        post.update(
            title = request.POST['title'],
            content = request.POST['content'],
            update_date = datetime.datetime.now(),
        )
        return redirect('home')
    post = Post.objects.get(pk=post_pk)
    return render(request, 'edit.html', {
        'post': post,
        })

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        found_user = User.objects.filter(username=username)
        if found_user:
            error = "이미 존재하는 아이디입니다."
            return render(request, 'registration/signup.html', {
                'error': error,
            })
        new_user = User.objects.create_user(
            username=username,
            password=password,
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        # return redirect('home')
        return redirect(request.GET.get("next", '/'))
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(request.GET.get("next", "/"))
        error = "아이디 또는 비밀번호가 일치하지 않습니다."
        return render(request, 'registration/login.html', {'error':error})
    return render(request, 'registration/login.html')

def kakao_login(request):
    return render(request, 'registration/kakao_login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def profile(request):
    return redirect('home')