from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
def converter(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))
