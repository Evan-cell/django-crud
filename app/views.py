from django.shortcuts import redirect, render

from .forms import todosForm
from .models import Todos

# Create your views here.

#todos
def todos(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    todo = Todos.objects.filter(title__icontains=search_query)
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
def updateTodo(request,pk):
    todo = Todos.objects.get(id=pk)
    form = todosForm(instance=todo)
    if request.method == 'POST':
        form = todosForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'create.html', context)

# delete todo
def deleteTodo(request,pk):
    todo = Todos.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    context = {'todo':todo}
    return render(request, 'delete.html', context)

