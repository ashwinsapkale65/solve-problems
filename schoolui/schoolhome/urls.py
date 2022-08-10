
from django.contrib import admin
from django.urls import path,include
from schoolhome import views

urlpatterns = [
    path('',views.register,name="register"),
    path('stulog',views.stulog,name="stulog"),
    path('studentprofile',views.studentprofile,name="studentprofile"),

 
    path('studentregistration',views.studentregistration,name="studentregistration"),
    path('teacherregistration',views.studentregistration,name="teacherregistration"),
    path('logoutstudent',views.logoutstudent,name="logoutstudent")

]