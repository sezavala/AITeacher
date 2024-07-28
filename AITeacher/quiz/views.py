from django.shortcuts import render

# Create your views here.
def quiz_page(request, quiz_name):
    context = {
        'quiz_name': quiz_name
    }
    return render(request, 'quiz/quiz.html', context)