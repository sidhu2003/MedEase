from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import SignupForm, LoginForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)    
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'user/signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')