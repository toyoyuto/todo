from django.http import HttpResponse

from django.shortcuts import render
import requests

    
def index(request):
    return HttpResponse("こんちには！")

def show(request):
    print("show")
    return render(request, 'todos/hello.html')

def get(request):
    print("get")
    url = 'http://127.0.0.1:8080/api/'
    r = requests.get(url)
    response = r.json()
    print("response", response)
    return render(request, 'todos/todos.html',  {'todos': response })
