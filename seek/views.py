from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request, "seek/index.html")


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successfully")
            return redirect(index)

        else:
            messages.error(request,"Name or password doesn't match.")
            return redirect(user_login)
        

    return render(request, "seek/login.html")


def user_logout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return redirect(index)

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")

        user=User.objects.filter(username=username,password=password).first()

        if user:
            messages.error(request,'Username already exists')

        elif len(username)<4:
            messages.error(request,'Name must be greater than 4 words')

        elif len(email)<4:
            messages.error(request,'Email must be greater than 4 words')


        elif len(password)<8:
            messages.error(request,'Password must be greater than 8 digits')


        elif password!=confirm_password:
            messages.error(request,"Password doesn't match")


        else:
            new_user=User.objects.create_user(username=username,email=email,password=password)
            new_user.save()
            messages.success(request,"Registation complete Successfully")
            return redirect(user_login)
            

    return render(request, "seek/signup.html")


def image_search(request):
    if request.user.is_authenticated:
        return render(request, "seek/image_search.html")

    else:
        return redirect(user_login)


def about(request):
    return render(request, "seek/about.html")




