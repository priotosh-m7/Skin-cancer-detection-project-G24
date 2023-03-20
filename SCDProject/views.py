from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

import os
def index(request):
    return render(request,'index.html')

def info(request):
    return render(request, 'knowledge.html')

def registration(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        icd = request.POST['icd']
        dob = request.POST['dob']
        gender = request.POST['gender']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect(user_login)

    return render(request,'about-us.html')

def upload(request):
    images = request.GET['image']
    img = Image.open(images)
    
    #image = request.FILES['image']
    params = {'img':images}
    return render(request,'contact-us.html',params)
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            params = {'user':username}
            login(request,user)
            return redirect(index)
        else:
            messages.error(request,"Bad Credentials")

    return render(request,'index.html')

def spare(request):
    return render(request,'contact-us.html')