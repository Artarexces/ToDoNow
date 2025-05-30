from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm, TaskForm
from .models import Task


## Creacion de usuarios

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})



## Inicio y cierre de session (login-logout)

class UserLoginView(LoginView):
    template_name = 'tasks/login.html'
    redirect_authenticated_user = True
    
def logout_view(request):
    logout(request)
    return redirect('login')


## Tareas 

@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render (request, 'tasks/task_list.html', {'tasks': tasks})


## Creacion de tarea

@login_required(login_url='login')
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render (request, 'tasks/task_form.html', {'form': form})


## Editar tarea 

@login_required(login_url='login')
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')        
    else:
        form = TaskForm(instance=task)
    return render (request, 'tasks/task_form.html', {'form': form, 'title':'Editar tarea'})


## Completar tarea

@login_required(login_url='login')
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')


## Eliminar tarea

@login_required(login_url='login')
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')
