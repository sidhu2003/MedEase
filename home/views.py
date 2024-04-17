from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    user = User.objects.all()
    return render(request,'home/index.html',{'user':user})

def aboutus(request):
    return render(request,'home/aboutus.html')

def diet(request):
    return render(request,'home/diet.html')

@login_required(login_url='login')
def prescription(request):
    return render(request,'home/prescription.html')

def video(request):
    return render(request,'home/video.html')

@login_required(login_url='login')
def dashboard(request):
    user = User.objects.all()
    return render(request,'home/dashboard.html')

@login_required(login_url='login')
def appointment(request):
    return render(request,'home/appointment.html')