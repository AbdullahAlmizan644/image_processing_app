from django.urls import path
from . import views


urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.user_login,name="login"),
    path("logout",views.user_logout,name="user_logout"),
    path("signup",views.signup,name="signup"),
    path("image_search",views.image_search,name="image_search"),
    path("face_search",views.face_search,name="face_search"),
    path("person_details",views.person_details,name="person_details"),
    path("about",views.about,name="about"),

]
