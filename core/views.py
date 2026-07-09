from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def home(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password =request.POST['password']
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return redirect('login')
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')