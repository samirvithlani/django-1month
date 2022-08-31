from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('a/',views.home),
    path('contactus/',views.contactus),
    path('aboutus/',views.aboutus),
    path('getEmployees/',views.getEmployees),
    
    
]
