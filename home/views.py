from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def aboutus(request):
    return render(request,'home/aboutus.html')

def diet(request):
    return render(request,'home/diet.html')

def prescription(request):
    return render(request,'home/prescription.html')

def video(request):
    return render(request,'home/video.html')

def dashboard(request):
    return render(request,'home/dashboard.html')

def appointment(request):
    return render(request,'home/appointment.html')