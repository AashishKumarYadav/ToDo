from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_compleated=False).order_by('-updated_at')
    #print(tasks)
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html',context)