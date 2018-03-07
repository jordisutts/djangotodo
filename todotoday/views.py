from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from.models import TodoItem
from .forms import TodoItemForm, EditTodoItemForm


# Create your views here.

def get_todo_page(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        print("its the get")
        
    form = TodoItemForm()
    items = TodoItem.objects.all()
    return render(request, "todo/todo-list.html", {'items':items, 'form':form})  
    
    
def delete_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.delete()
    return redirect("/")
    
def toggle_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    item.done = not item.done
    item.save()
    return redirect("/")
    
def edit_todo_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    
    if request.method == "POST":
        form = EditTodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        print("Get")
        
    
    form = EditTodoItemForm(instance=item)
    items = TodoItem.objects.all()
    return render(request, "todo/todo-item-edit.html", {'items':items, 'form':form}) 