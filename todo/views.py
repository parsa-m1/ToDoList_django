from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Todo
from .forms import TodoForm

def todos_list(request):
    todos = Todo.objects_recent.all()
    if request.method == 'POST':
        print(request.POST)
        id = request.POST['done_todo']
        todo = get_object_or_404(Todo, id=id)
        todo.is_done = True
        todo.save()
        return redirect('todos_list')

    return render(request, 'todos_list.html', {'todos': todos})

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


def create(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos_list')

    return render(request, 'create.html', {'form': form})


def update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos_list')

    return render(request, 'create.html', {'form': form})


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    delete(request, todo)
    return redirect('todos_list')







