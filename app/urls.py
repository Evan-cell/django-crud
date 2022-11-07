from django.urls import path

from . import views

urlpatterns = [
    
    path('todo/', views.todos, name="todos"),
    path('create/',views.createTodo, name="create"),
    path('update/<str:pk>/',views.updateTodo, name="update"),
    path('delete/<str:pk>/',views.deleteTodo, name="delete"),
    path('', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout', views.logout_request, name= "logout")
]