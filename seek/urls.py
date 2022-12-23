from django.urls import path
from . import views


urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.user_login,name="login"),
    path("logout",views.user_logout,name="user_logout"),
    path("signup",views.signup,name="signup"),
    path("image_search",views.image_search,name="image_search"),
    path("about",views.about,name="about"),

]
