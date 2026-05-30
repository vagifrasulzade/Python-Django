from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register__view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Siz ugurla register olduz!")
            return redirect("home")

        else:
            messages.warning(request, "username ve ya parol sehvdir")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def login__view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Siz ugurla daxil oldunuz!")
            return redirect("home")

        else:
            messages.error(request, "username ve ya parol sehvdir")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def logout__view(request):
    logout(request)
    messages.success(request, "Siz ugurla cixis etdiniz!")
    return redirect("home")


@login_required
def change_password__view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Parolunuz ugurla deyisdirildi!")
            return redirect("home")
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, "change_password.html", {"form": form})


