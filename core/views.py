from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
    if request.method == "POST":
        username_input = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username_input,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def add_task(request):
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        description = request.POST.get('description')

    return render(request, 'add_task.html')