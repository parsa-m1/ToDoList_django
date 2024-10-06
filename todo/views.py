from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Todo

def todos_list(request):

    return render(request, 'todos_list.html')

def index(request):
    todos = Todo.objects_recent.all()

    return render(request, 'index.html')


def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('todos_list')

    return render(request, 'register.html', {"form": form})


def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todos_list')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('index')








