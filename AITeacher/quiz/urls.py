from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('<str:quiz_name>_quiz/', views.quiz_page, name='quiz_page'),
    # Other URL patterns
]