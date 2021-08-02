from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout

# Create your views here.

def index(request):
    return render(request,'user/index.html',context={})

def registration_view(request):
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'registration successfull')
            return HttpResponseRedirect(reverse('Usermodule:index'))
    else:
        form = CustomUserCreationForm
    return render(request, 'user/registration.html',context={'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'Login Successfull')
            return HttpResponseRedirect(reverse('Usermodule:index'))
            
        else:
            messages.warning(request,"Username and Password doesn't match")
    return render(request,'user/login.html')
    
@login_required
def logout_view(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('Usermodule:index')


