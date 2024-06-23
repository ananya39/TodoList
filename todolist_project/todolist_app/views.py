# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

def index(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoItemForm()
    
    items = TodoItem.objects.filter(completed=False)
    return render(request, 'todolist_app/index.html', {'form': form, 'items': items})

def mylist(request):
    items = TodoItem.objects.filter(completed=True)
    return render(request, 'todolist_app/mylist.html', {'items': items})

def mark_as_completed(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    item.completed = True
    item.save()
    return redirect('index')

def delete_item(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    item.delete()
    return redirect('mylist')

def edit_item(request,item_id):
    item=get_object_or_404(TodoItem,id=item_id)
    if request.method=="POST":
        form=TodoItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=TodoItemForm(instance=item)
    return render(request,'todolist_app/edit_item.html',{'form': form})
