from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html', {
        'majors': majors,
        'subjects': subjects,
    })

# def computer(request):
#     computers_major = Major.objects.filter(name="컴퓨터학과")
#     #computers_subject = Subject.objects.filter(major="컴퓨터학과")
#     computers_subject = Subject.objects.filter(major=4)

#     # computers_subject = Subject.objects.all()
#     # print(computers_subject.major.name)

#     return render(request, 'computer.html', {
#         'computers_major': computers_major,
#         'computers_subject': computers_subject,
#     })

def major(request, major_pk):
    major = Major.objects.get(pk = major_pk)
    lectures = Subject.objects.filter(major=major_pk)

    return render(request, 'major.html', {
        'major': major,
        'lectures': lectures,
    })

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def deleteSubject(request, subject_pk):
    subject = Subject.objects.get(pk=subject_pk)
    subject.delete()
    return redirect('home')

class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')

def deleteMajor(request, major_pk):
    major = Major.objects.get(pk=major_pk)
    major.delete()
    return redirect('home')