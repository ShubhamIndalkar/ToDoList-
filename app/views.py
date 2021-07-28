from app.models import Task
from django.shortcuts import render,redirect

from app.forms import TodoForm

# Create your views here.
def index(request):
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(todo)

    else:
        form = TodoForm(request.POST)
    return render(request,'index.html',{"form":form})   

def todo(request):
    read = Task.objects.all()
    return render(request,'tasks.html',{"read":read}) 

def Update(request,id):
    upd = Task.objects.get(id=id)
    update = TodoForm(request.POST or None , request.FILES or None , instance=upd)
    if update.is_valid():
        update.save()
        return redirect (todo)
    return render(request,"update.html",{"update":update})

def Delete(request,id):
    del_t=Task.objects.get(id=id)    
    del_t.delete()
    return redirect(todo)

