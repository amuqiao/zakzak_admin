# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html')


# http://127.0.0.1:8000/add/?a=400&b=500
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


# http://127.0.0.1:8000/add/1/2/
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
