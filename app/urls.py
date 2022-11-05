from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.todos, name="todos"),
    path('create/',views.createTodo, name="create"),
    path('update/<str:pk>/',views.updateTodo, name="update"),
    path('delete/<str:pk>/',views.deleteTodo, name="delete"),
]