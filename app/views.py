from django.shortcuts import redirect, render

from .forms import todosForm
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
    form = todosForm()
    if request.method == 'POST':
        form = todosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    
    context={'form':form}
    return render(request, 'create.html', context)
    
#update todo
def updateTodo(request):
    context = {}
    return render(request, 'update.html', context)

# delete todo
def deleteTodo(request):
    context = {}
    return render(request, 'delete.html', context)

