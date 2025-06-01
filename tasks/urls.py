from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('tasks/<int:pk>/delete', views.task_delete, name='task_delete'),
]