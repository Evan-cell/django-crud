from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.todos, name="todos"),
    path('create/',views.createTodo, name="create"),
    path('update/',views.updateTodo, name="update"),
    path('delete/',views.deleteTodo, name="delete"),
]