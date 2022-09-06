from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('a/',views.home),
    path('contactus/',views.contactus),
    path('aboutus/',views.aboutus),
    path('getEmployees/',views.getEmployees),
    path('addstudent/',views.StudentView.as_view(),name='addstudent'),
    path('studentlist/',views.StudentListView.as_view(),name='studentlist'),
    path('deletestudent/<int:pk>',views.StudentDeleteView.as_view(),name='deletestudent'),
    path('studentdetail/<int:pk>',views.StudentDetailView.as_view(),name='studentdetail'),
    path('studentupdate/<int:pk>',views.StudentUpdateView.as_view(),name='studentupdate'),
    
    
]
