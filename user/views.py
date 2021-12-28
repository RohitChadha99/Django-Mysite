from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'user/login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'Sign-in successfully')
            return render(request,'user/logout.html',{'name': username , 'email' : user.email})
        else:
            messages.error(request,'Invalid User info')
            return redirect('home')

def signup(request):
    return render(request,'user/signup.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request,'Passwords do not match.')
            return redirect('home')

        if len(pass1)<=3:
            messages.warning(request,'Password must be altleast Four characters.')
            return redirect('home')

        if len(username)>10:
            messages.warning(request,'Username not exceeds Ten characters.')
            return redirect('home')
        
        if User.objects.filter(username = username).exists():
            messages.warning(request,'Username already exist')
            return redirect('home')

        if User.objects.filter(email = email).exists():
            messages.warning(request,'Email already registered please try another one.')
            return redirect('home')

        if not username.isalnum():
            messages.warning(request,'Username must be alphanumeric')
            return redirect('home')
        

        user = User.objects.create_user(username,email,pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()


        messages.success(request,'Your account has been created successfully.')
        return redirect('home')

def handlesignout(request):
    logout(request)
    messages.success(request,'Sign out successfully')
    return redirect('home')


def logout(request):
    return render(request,'user/logout.html')