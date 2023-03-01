from django.urls import path
from . import views


urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.user_login,name="login"),
    path("logout",views.user_logout,name="user_logout"),
    path("signup",views.signup,name="signup"),
    path("fingerprint_search",views.fingerprint_search,name="fingerprint_search"),
    path("face_search",views.face_search,name="face_search"),
    path("test_search",views.test_search,name="test_search"),
    path("person_details",views.person_details,name="person_details"),
    path("about",views.about,name="about"),
    path("profile",views.profile,name="profile"),
    path("add_user_data",views.add_user_data,name="add_user_data"),
    path("nid_search",views.nid_search,name="nid_search"),
    path("nid_number_search",views.nid_number_search,name="nid_number_search"),
    path("user_message",views.user_message,name="user_message"),
]
