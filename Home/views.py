from django.shortcuts import render, HttpResponse,redirect
from .forms import *
from .models import *

# Create your views here.
 
def home(request):
    task = Task.objects.all()
    #create Form object
    form = ToDoForm()
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')      
        
    context ={'task':task,'form':form}
    return render(request,'index.html',context)

def updateList(request,pkid):
    task = Task.objects.get(id = pkid)
    form = ToDoForm(instance=task)
    if request.method == "POST":
        form = ToDoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')     
    context = {'form':form}
    return render(request,'update.html',context)

def deleteList(request,pkid):
    task = Task.objects.get(id = pkid)
    form = ToDoForm(instance = task)
    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {'task':task}
    return render(request,'delete.html',context)