from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# password of ronish user is Ronish@@@111
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    messages.success(request, "This is a test message")
    return render (request, "index.html")
    # return HttpResponse("This is my new site")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method== "POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        contact= Contact(name=name, email=email, desc=desc, phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, "Profile details updated.")
    return render(request, "contact.html")

def services(request):
    return HttpResponse("This is my services site")

def options(request):
    return render(request, "options.html")

def tour(request):
    return render(request, "tour.html")

def view(request):
    return render(request, "view.html")

def loginUser(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        # A backend authenticated the credentials
            return redirect("/")
    
        else:
         # No backend authenticated the credentials
            return render(request, "login.html")
    
        #check f user has entered correct credentials
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")



