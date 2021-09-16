from django.shortcuts import render, redirect


def HomePage(request):
    return render(request,'MainApplication/public/Home.html' )



def PublicAboutUs(request):
    return render(request,'MainApplication/public/AboutUs.html' )



def PublicContactUs(request):
    return render(request,'MainApplication/public/ContactUs.html' )




def Login(request):
    return render(request,'MainApplication/LogIn.html')




def SignUp(request):
    return render(request, 'MainApplication/SignUp.html')