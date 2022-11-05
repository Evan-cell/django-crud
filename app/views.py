from django.shortcuts import render

from .models import Todos

# Create your views here.

#todos
def todos(request):
    todo = Todos.objects.all()
    print(todo)
    context = {'todo':todo}
    return render(request, 'todos.html', context)




#create todo
def createTodo(request):
    context = {}
    return render(request, 'create.html', context)
    
#update todo
def updateTodo(request):
    context = {}
    return render(request, 'update.html', context)

# delete todo
def deleteTodo(request):
    context = {}
    return render(request, 'delete.html', context)

