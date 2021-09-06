from django.shortcuts import render
from personal.models import Question
# Create your views here.

def home_screan_view(request):


    questions = Question.objects.all()
    content = {
        "questions": questions
    }
    return render(request,"personal/home.html",content)
