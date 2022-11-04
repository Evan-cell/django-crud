from django.shortcuts import render

# Create your views here.

#todos
def todos(request):
    context = {}
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

