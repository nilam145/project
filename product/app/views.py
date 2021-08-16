from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.


def sign_up(request):
    if request.method == "POST":
        fm = UserRegisterForm(request.POST)
        if fm.is_valid():
            fm.save()

            messages.success(request, f'Your account has been created ! You are now able to log in')
            return HttpResponseRedirect('/login/')
    else:
        fm = UserRegisterForm()
    return render(request, 'app/signup.html', {"form": fm})


def Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Logged in successfully!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'app/login.html', {"form": fm})
    else:
        return HttpResponseRedirect('/profile/')


def Profile(request):
    if request.user.is_authenticated:
        return render(request, 'app/profile.html',{'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')





