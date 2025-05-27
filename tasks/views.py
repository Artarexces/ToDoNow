from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, aauthenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, TaskForm
from .models import Task



