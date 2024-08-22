from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("register",views.register,name="register"),
    path("my_login",views.my_login,name="my_login"),
    path("my_logout",views.user_logout,name="my_logout"),
]