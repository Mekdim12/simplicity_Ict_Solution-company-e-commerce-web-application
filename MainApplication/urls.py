
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.HomePage, name='main'),
    path('public/aboutus',views.PublicAboutUs , name ='PublicAboutUs'),
    path('public/contactus', views.PublicContactUs, name ='PublicContactUs'),
    path('login', views.Login, name ='logins'),
    path('signup',views.SignUp, name = 'signup')
]
