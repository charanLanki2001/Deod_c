from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required




#@login_required(login_url='login')
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        
        pass3=request.POST.get('password')
        
        user=authenticate(request,username=username,password=pass3)
        
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
           return HttpResponse("Username or password is not correct!!")
    return render(request,'login.html')

def Homepage(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST.get('Username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("<h1>incorrect password in password and confirm password!!<h1>")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('loginpage')
    return render(request,'signup.html')
def video(request):
    return render(request,'video.mp4')