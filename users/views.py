from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:product_list')
                
            else:
                messages.error(request, 'Invalid Credentials')
        else:
            messages.error(request, 'Error! Try Again')
    else:
        form  = LoginForm()
    return render(request, 'users/login.html', {'form':form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('shop:product_list')
        else:
            messages.error(request, 'Error')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required(login_url='/users/login')
def logout_view(request):
    logout(request)
    return render(request, 'users/login.html')        