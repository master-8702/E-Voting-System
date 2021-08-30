from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'systemuser/index.html')

def index1(request):
    return render(request, 'systemuser/index1.html')