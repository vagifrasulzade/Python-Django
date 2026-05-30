from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("login/", views.login__view, name="login"),
    path("register/", views.register__view, name="register"),
    path("logout/", views.logout__view, name="logout"),
    path("password-change/", views.change_password__view, name="password_change"),
]
