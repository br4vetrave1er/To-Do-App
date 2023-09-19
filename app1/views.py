from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from app1.models import Task
# Create your views here.


def homepage(request):
    return render(request,"index.html")

def todo(request):
    incomplete_task = Task.objects.filter(is_completed=False).order_by("-modified_at")
    completed_task = Task.objects.filter(is_completed=True).order_by("-modified_at")
    context = {
        "Tasks_completed" : completed_task,
        "Tasks_incomplete": incomplete_task
    }
    return render(request, "home-todo.html", context)

def add_task(request):
    new_task = request.POST['task']
    Task.objects.create(task=new_task)
    return redirect("todo")

def mark_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("todo")

def mark_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect("todo")

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        
        return redirect("todo")
    else:
        context = {
            'get_task' : get_task
        }
        
        return render(request, "edit_task.html", context)
    
def delete_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    
    return redirect("todo")