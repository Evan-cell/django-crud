from django.urls import path

from . import views
from .views import TodoDetailApiView, todoListApi

urlpatterns = [
    
    path('', views.todos, name="todos"),
    path('create/',views.createTodo, name="create"),
    path('update/<str:pk>/',views.updateTodo, name="update"),
    path('delete/<str:pk>/',views.deleteTodo, name="delete"),
    path('register', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout', views.logout_request, name= "logout"),
    path('api', todoListApi.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]