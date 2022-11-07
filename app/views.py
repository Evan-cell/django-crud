from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import NewUserForm, todosForm
from .models import Todos

# Create your views here.

#todos
@login_required(login_url='login')
def todos(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    todo = Todos.objects.filter(title__icontains=search_query)
    print(todo)
    context = {'todo':todo}
    return render(request, 'todos.html', context)




#create todo
@login_required(login_url='login')
def createTodo(request):
    form = todosForm()
    if request.method == 'POST':
        form = todosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')    

    
    context={'form':form}
    return render(request, 'create.html', context)
    
#update todo
@login_required(login_url='login')
def updateTodo(request,pk):
    todo = Todos.objects.get(id=pk)
    form = todosForm(instance=todo)
    if request.method == 'POST':
        form = todosForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    context = {'form':form}
    return render(request, 'create.html', context)

# delete todo
@login_required(login_url='login')
def deleteTodo(request,pk):
    todo = Todos.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos')
    context = {'todo':todo}
    return render(request, 'delete.html', context)
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('todos')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'auth/signup.html', context={"register_form":form})    
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("todos")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"auth/login.html", context={"login_form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')