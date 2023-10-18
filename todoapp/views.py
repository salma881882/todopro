from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from .forms import TodoForm
from django.views.generic import ListView, UpdateView
from django.views.generic import DetailView,DeleteView

#Clas
class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task2'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('tname','tpriority','tdate')

    def get_success_url(self):
        return reverse_lazy('dbv',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('clsbsdhom')








# Create your views here.
def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')

        task=Task(tname=name,tpriority=priority,tdate=date)
        task.save()
    return render(request,'index.html',{'task2':task1})

# def details(request):
#
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    ttask=Task.objects.get(id=id)
    tform=TodoForm(request.POST or None, instance=ttask)
    if tform.is_valid():
        tform.save()
        return redirect('/')
    return render(request,'edit.html',{'tf':tform,'taskk':ttask})


#vrtlenv:(todopo)