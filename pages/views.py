from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeViewPage(request):
    x = f"<h1>Hello World</h1><h2>subtitle1</h2><h2>subtitle2</h2>"
    return HttpResponse(x)
