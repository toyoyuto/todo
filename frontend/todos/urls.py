from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('todo', views.todo, name='todo'),
    path('<int:todo_id>', views.detail, name='detail'),
]
