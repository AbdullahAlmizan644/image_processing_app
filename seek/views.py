from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "seek/index.html")


def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username=username,password=password)
        
        if user:
            request.session['user'] = username
            messages.success(request,"Login successfully")
            return redirect(index)

        else:
            messages.error(request,"Name or password doesn't match.")

    return render(request, "auth/login.html")


def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        print(username,email,password1,password2)

        if len(username)<4:
            messages.error(request,'Name must be greater than 4 words')

        elif len(email)<4:
            messages.error(request,'Email must be greater than 4 words')



        elif len(password1)<8:
            messages.error(request,'Password must be greater than 8 words')


        elif password1!=password2:
            messages.error(request,"Password doesn't match")


        else:
            user=User(username=username,email=email,password=password1)
            user.save()
            messages.success(request,"Registation complete Successfully")
            return redirect(login)
            

    return render(request, "auth/signup.html")


def image_search(request):
    if "user" in request.session:
        return render(request, "seek/image_search.html")
    else:
        return redirect(login)


def about(request):
    return render(request, "seek/about.html")


def logout_user(request):
    del request.session['user']
    return redirect(login)