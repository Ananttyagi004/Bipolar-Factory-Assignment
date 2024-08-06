from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.signup, name="register"),
    path("userlogin/", views.user_login, name="user-login"),
    path("adminlogin/", views.admin_login, name="admin-login"),
    path("logout/", views.custom_logout, name="logout"),]