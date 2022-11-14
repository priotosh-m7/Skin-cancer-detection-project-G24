from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render(request,'index.html')

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
        return redirect(login)

    return render(request,'about-us.html')

def upload(request):
    return render(request,'features.html')
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
        else:
            messages.error(request,"Bad Credentials")

    return render(request,'index.html')