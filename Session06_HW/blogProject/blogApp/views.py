from pickletools import read_uint1
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def home(request):
    return render(request, 'home.html')

def new(request):
    if request.method == 'POST':
        #POST 요청으로 온 데이터 확인
        print(request.POST)
        Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    count_coding = len(Article.objects.filter(category='coding'))
    count_hobby = len(Article.objects.filter(category='hobby'))
    count_food = len(Article.objects.filter(category='food'))
    return render(request, 'list.html', {
        'articles': articles,
        'count_coding': count_coding,
        'count_hobby': count_hobby,
        'count_food': count_food,
        })

def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article':article})

def detail_delete(request, article_id):
    Article.objects.filter(id = article_id).delete()
    return redirect('list')

def listcat(request, article_cat):
    articles = Article.objects.filter(category = article_cat)
    articlecount = 0
    for article in articles:
        articlecount += 1
    return render(request, 'listcat.html', {
        'articles': articles,
        'articlecount': articlecount,
        'article_cat': article_cat,
        })