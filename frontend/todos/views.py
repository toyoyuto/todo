from django.http import HttpResponse

from django.shortcuts import render
import requests

    
def index(request):
    print("index")
    return render(request, 'todos/index.html')

def hello(request):
    print("hello")
    return render(request, 'todos/hello.html')

def todo(request):
    print("todo")
    url = 'http://127.0.0.1:8080/api/'
    r = requests.get(url)
    response = r.json()
    print("response", response)
    return render(request, 'todos/todos.html',  {'todos': response })

def detail(request, todo_id):
    print(detail)
    print(todo_id)
    url = 'http://127.0.0.1:8080/api/' + str(todo_id)
    r = requests.get(url)
    response = r.json()
    print("response", response)
    return render(request, 'todos/detail.html',  {'todo': response })
