from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.aboutus,name="about"),
    path('appointment/',views.appointment,name="appointment"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('diet/',views.diet,name="diet"),
    path('prescription/',views.prescription,name="prescription"),
    path('video/',views.video,name="video")
]