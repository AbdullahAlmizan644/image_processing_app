from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import cv2
import numpy as np
import os
from image_processing_app.settings import PROJECT_ROOT,STATICFILES_DIRS
from .models import Person
import face_recognition
from .models import Person
from django.core.files.storage import FileSystemStorage

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


def fingerprint_search(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            image = request.POST['image']
            print(image)
            
            original = cv2.imread(f"/home/zeus/Desktop/{image}",0)
            print(original)

            persons=Person.objects.all()
            all_image=[p.person_image for p in persons]

            count=0
            for single_image in all_image:
                print(single_image)
                duplicate = cv2.imread(f"{single_image}",0)
                print(duplicate)



                if original.shape == duplicate.shape:
                    print("The images have same size and channels")
                    difference = cv2.subtract(original, duplicate)
                    print(difference)
                    print(count)
                    # b, g, r = cv2.split(difference)

                    if cv2.countNonZero(difference[count]) == 0 and cv2.countNonZero(difference[count+1]) == 0 and cv2.countNonZero(difference[count+2]) == 0:
                        print("The images are completely Equal")
                        # cur=db.connection.cursor()
                        # cur.execute("select * from person where image=%s",(a,))
                        # result=cur.fetchone()
                        result=Person.objects.filter(person_image=single_image).first()
                        print(result)
                        break

                else:
                    print("the images are not equal")
                    result=0
            
                count=count+3
            
            if result==0:
                messages.error(request,"no person on that image")
                return redirect(fingerprint_search)
        
            return render(request,"seek/person_details.html",{
                "result":result,
            })
        return render(request, "seek/fingerprint_search.html")

    else:
        return redirect(user_login)


    
def face_search(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            image = request.POST['image']
            print(image)

            unknown_image = face_recognition.load_image_file(f"/home/zeus/Desktop/{image}",)


            persons=Person.objects.all()
            all_image=[p.person_image for p in persons]
            
            try:
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            except IndexError:
                messages.error(request,"Please give a person image not any fictional object")
                return redirect(face_search)

            for single_image in all_image:
                print(single_image)
                known_image = face_recognition.load_image_file(f"media/{single_image}")
                known_encoding = face_recognition.face_encodings(known_image)[0]
                r = face_recognition.compare_faces([known_encoding], unknown_encoding)
                print(r)
            
                if r==[True]:
                    # print(known_encoding)
                    # print(unknown_encoding)
                    result=Person.objects.filter(person_image=single_image).first()
                    return render(request,"seek/person_details.html",{
                        "result":result,
                        })

            messages.error(request,"Not found same face person ")
            return redirect(face_search)
        return render(request, "seek/face_search.html")

    else:
        return redirect(user_login)

def person_details(request):
    if request.user.is_authenticated:
        return render(request, "seek/person_details.html")

    else:
        return redirect(user_login)


def about(request):
    return render(request, "seek/about.html")


def profile(request):
    if request.user.is_authenticated:
        return render(request, "seek/profile.html",{
            "user":request.user,
        })

    else:
        return redirect(user_login)



def add_user_data(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            email=request.POST.get("email")
            division=request.POST.get("division")
            district=request.POST.get("district")
            address=request.POST.get("address")
            present_address=request.POST.get("present_address")
            about=request.POST.get("about")
            gender=request.POST.get("gender")
            nid_number=request.POST.get("nid_number")
            date=request.POST.get("date")
            personal_number=request.POST.get("personal_number")
            relative_number=request.POST.get("relative_number")
            emergency_number=request.POST.get("emergency_number")
            # =request.POST.get("")



            #images
            person_image=request.FILES["person_image"]
            nid_image=request.FILES["nid_image"]
            fingerprint_image=request.FILES["fingerprint_image"]

            fss=FileSystemStorage()

            person_image_file=fss.save(person_image.name, person_image)
            person_image_url=fss.url(person_image_file)


            nid_image_file=fss.save(nid_image.name, nid_image)
            nid_image_url=fss.url(nid_image_file)

            fingerprint_image_file=fss.save(fingerprint_image.name, fingerprint_image)
            fingerprint_image_url=fss.url(fingerprint_image_file)




            person_data=Person(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    division=division,
                    district=district,
                    address=address,
                    present_address=present_address,
                    about=about,
                    gender=gender,
                    nid_number=nid_number,
                    nid_image=nid_image_url,
                    person_image=person_image_url,
                    fingerprint_image=fingerprint_image_url,
                    date=date,
                    personal_number=personal_number,
                    relative_number=relative_number,
                    emergency_number=emergency_number)

            person_data.save()
            messages.success(request, "Your data add successfully")
            return redirect("/")
            
        return render(request, "seek/add_user_data.html",{
            "user":request.user,
        })

    else:
        return redirect(user_login)




    
def nid_search(request):
    return render(request,"nid.html")



def user_message(request):
    pass
