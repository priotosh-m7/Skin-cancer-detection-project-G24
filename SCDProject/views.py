from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def registration(request):
    return render(request,'about-us.html')

def upload(request):
    return render(request,'features.html')