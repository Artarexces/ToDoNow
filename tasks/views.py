from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
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

# class UserLoginView(SuccessMessageMixin, LoginView):
#     template_name = 'tasks/login.html'
#     success_message = '¡Inicio de sesión exitoso!'
#     redirect_authenticated_user = True
    
def login_view(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "Usuario o contraseña incorrecto.")
    return render(request, 'tasks/login.html')
    
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Cerraste sesión correctamente.')
    return redirect('login')

 
## Lista de tareas

@login_required(login_url='login')
def task_list(request):
    section = request.GET.get('section', 'all')
    if section == 'pendientes':
        tasks = Task.objects.filter(user=request.user, completed=False).order_by('due_date')
    elif section == 'completadas':
        tasks = Task.objects.filter(user=request.user, completed=True).order_by('due_date')
    else:
        tasks = Task.objects.filter(user=request.user).order_by('due_date')
    return render (request, 'tasks/task_list.html', {'tasks': tasks, 'section': section})


## Crear tarea

@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render (request, 'tasks/add_task.html', {'form': form})


## Editar tarea 

@login_required(login_url='login')
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')        
    else:
        form = TaskForm(instance=task)
    return render (request, 'tasks/edit_task.html', {'form': form, 'title':'Editar tarea'})


## Completar tarea

@login_required(login_url='login')
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


## Eliminar tarea

@login_required(login_url='login')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})