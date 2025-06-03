from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(blank=True, verbose_name='Descripción')
    due_date = models.DateTimeField(verbose_name='Fecha y hora',null=True,    # permitimos que exista sin fecha al principio
        blank=True,
        default=None)
    priority = models.BooleanField(default=False, verbose_name='Prioridad')
    completed = models.BooleanField(default=False, verbose_name='Completada')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title