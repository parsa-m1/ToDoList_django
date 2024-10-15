from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects_recent.all()
    if request.method == 'POST':
        id = request.POST['done_todo']
        todo = get_object_or_404(Todo, id=id)
        todo.is_done = True
        todo.save()
        return redirect('index')

    return render(request, 'index.html', {'todos': todos})

def todo_detail(request, slug):
    todo = get_object_or_404(Todo, slug=slug)

    if request.method == 'POST':
        status = request.POST['status']
        if  status == 'done':
            todo.is_done = True
        elif status == 'undone':
            todo.is_done = False
        todo.save()
        return redirect('index')


    return render(request, 'todo_detail.html', {'todo': todo})


def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('index')

    return render(request, 'register.html', {"form": form})


def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

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
            todo.slug = slugify(todo.title)
            todo.save()
            return redirect('index')

    return render(request, 'create.html', {'form': form})


def update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'create.html', {'form': form})


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    delete(request, todo)
    return redirect('index')






