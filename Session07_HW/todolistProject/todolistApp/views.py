from django.shortcuts import render
from .models import Todo
from django.shortcuts import redirect
from datetime import date
from operator import attrgetter

# Create your views here.

def home(request):
    items = Todo.objects.all().order_by('due')
    dday_dic = {}
    for item in items:
        today = date.today()
        dday = date(item.due.year, item.due.month, item.due.day)
        dday = (today - dday).days
        dday_dic[item.id] = dday
    dday_dic = dday_dic.items()

    if request.method == 'POST':
        Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due'],
            )
        return redirect('home')
    return render(request, 'home.html', {
        'items': items,
        'dday_dic': dday_dic,
    })

def detail(request, item_id):
    item = Todo.objects.get(id=item_id)
    dday = (date.today() - date(item.due.year, item.due.month, item.due.day)).days
    return render(request, 'detail.html', {
        'item': item,
        'dday': dday,
    })

def edit(request, item_id):
    item = Todo.objects.get(id=item_id)
    if request.method == 'POST':
        Todo.objects.filter(id=item_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due'],
        )
        return redirect('home')
    return render(request, 'edit.html', {
        'item': item,
    })

def editsimple(request, item_id):
    item = Todo.objects.get(id=item_id)
    items_except = Todo.objects.exclude(id=item_id).order_by('due')

    dday_dic = {}
    for item_except in items_except:
        today = date.today()
        dday = date(item_except.due.year, item_except.due.month, item_except.due.day)
        dday = (today - dday).days
        dday_dic[item_except.id] = dday
    dday_dic = dday_dic.items()

    if request.method == 'POST':
        Todo.objects.filter(id=item_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
            due = request.POST['due'],
        )
        return redirect('home')
    return render(request, 'editsimple.html', {
        'item': item,
        'items_except': items_except,
        'dday_dic': dday_dic,
    })

def delete(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    return redirect('home')