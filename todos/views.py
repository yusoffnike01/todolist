from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def list_todo_item(request):
    content={'todo_list' : Todo.objects.all()}
    return render(request,'todos/todo_list.html',content)

def insert_todo_item(request:HttpRequest):
     
     todo=Todo(content=request.POST['content'])
     todo.save()
     return redirect('/todos/list/')
def delete_todo_item(request, todo_id):
    todo_to_delete=Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')

def register_user(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'todos/register.html',{'form': form})

def login_user(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/todos/list/')
    else:
        form=AuthenticationForm()
    return render(request,'todos/login.html',{'form': form})




