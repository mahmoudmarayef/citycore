from django.shortcuts import render
from .models import TodoItem
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

def home(request):
    return render(request, 'index.html')

def projects(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'projects.html', {'all_items': all_todo_items})
