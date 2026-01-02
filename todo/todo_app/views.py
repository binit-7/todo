from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def home(request):  
    task = Task.objects.filter(is_completed=False).order_by('-updated_at') # filter is used to fetch multiple data with different conditions
    context = {
        'task' : task
    }
    return render(request, 'home.html', context)

def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')    

