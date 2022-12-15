from django.urls import path
from . import views


urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("image_search",views.image_search,name="image_search"),
    path("about",views.about,name="about"),
    path("logout_user",views.logout_user,name="logout_user"),
]
