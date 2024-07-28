from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse

# Create your views here.

def home(request):
    context = {
        'quizzes': [
            {'name': 'Javascript', 'url': reverse('quiz:quiz_page', kwargs={'quiz_name': 'Javascript'})},
            {'name': 'Java', 'url': reverse('quiz:quiz_page', kwargs={'quiz_name': 'Java'})},
            {'name': 'Python', 'url': reverse('quiz:quiz_page', kwargs={'quiz_name': 'Python'})},
            {'name': 'C', 'url': reverse('quiz:quiz_page', kwargs={'quiz_name': 'C'})},
            {'name': 'SQL', 'url': reverse('quiz:quiz_page', kwargs={'quiz_name': 'SQL'})},
            {'name': 'GoLang', 'url': reverse('quiz:quiz_page', kwargs={'quiz_name': 'GoLang'})},
        ]
    }
    return render(request, 'home/home.html', context)

def grid_click(request):
    return redirect('quiz:quiz_page')