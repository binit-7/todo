from multiprocessing import context
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Task
# Create your views here.
def home(request):  
    task = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True).order_by('-updated_at') # filter is used to fetch multiple data with different conditions
    context = {
        'task' : task,
        'completed_task' : completed_task
    }
    return render(request, 'home.html', context)

def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')

def delete_task(request, id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect('home')

def mark_complete(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_undone(request,id):
    task = get_object_or_404(Task,id=id)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, id):
    get_task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')

    
    else:
        return render(request, 'edit_task.html', {'task': get_task})