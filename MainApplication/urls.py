
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.HomePage, name='main'),
    path('public/aboutus',views.PublicAboutUs , name ='PublicAboutUs'),
    path('public/contactus', views.PublicContactUs, name ='PublicContactUs'),
    path('login/', views.Login, name ='login'),
    path('signup',views.SignUp, name = 'signup'),
    path('public/dashboard',views.dashBoard, name="dashboard"),
    path('public/shop',views.Shop, name="shop"),
    path('public/cart',views.Cart, name="cart"),
    path('public/nocart',views.NoCart, name="nocart"),
    path('private/staff/dashboardstaff',views.DashBoardStaff, name="dashboardstaff")

]
