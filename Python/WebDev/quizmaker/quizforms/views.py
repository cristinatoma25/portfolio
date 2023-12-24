from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

def homepage(request):
    quizes = Quiz.objects.all()

    if request.method == "POST":
        form = QuizCreationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            difficulty = form.cleaned_data['difficulty']
            Quiz.objects.create(name=name)
            form.save()
        return redirect('/')

    return render(request, 'homepage.html', {'request' : request})


