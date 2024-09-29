from django.shortcuts import render

from .models import Todo

def index(request):
    todos = Todo.objects_recent.all()

    return render(request, 'index.html')


