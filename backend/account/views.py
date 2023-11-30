from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from main.utils import fancy_message
from .forms import StylesCustomUserCreationForm
from .decorators import unauthenticated_user
from django.utils.translation import gettext as _


# Create your views here.

@unauthenticated_user
def user_login(request, *args, **kwargs):
    next = request.GET.get("next", None)
    if request.method == "POST":
        username_data = request.POST.get("username")
        password_data = request.POST.get("password")
        if username_data and password_data:
            user = authenticate(request, username=username_data, password=password_data)
            if user:
                login(request, user)
                fancy_message(request, f"welcome {user.username}", level="success")
                if next:
                    return redirect(next)
                else:
                    return redirect("main:dashboard")
            else:
                fancy_message(request, _("Username or Password is incorrect"), level="error")
                return redirect(request.META["HTTP_REFERER"])
        else:
            fancy_message(request, _("Username and Password is required"), level="error")
            return redirect(request.META["HTTP_REFERER"])
    my_context = {
        "Title": "Login"
    }

    return render(request, 'login.html', my_context)


@unauthenticated_user
def user_register(request, *args, **kwargs):
    if request.method == "POST":
        form = StylesCustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            fancy_message(request, _(f"welcome {user.username}"))
            return redirect("main:dashboard")
        else:
            fancy_message(request, form.errors, level="error")
    previous_data = {
        "first_name": request.POST.get("first_name", None),
        "last_name": request.POST.get("last_name", None),
        "email": request.POST.get("email", None),
        "username": request.POST.get("username", None),
    }
    form = StylesCustomUserCreationForm(initial=previous_data)
    my_context = {
        "Title": "Register",
        "form": form
    }

    return render(request, 'register.html', my_context)


@login_required
def user_logout(request, *args, **kwargs):
    logout(request)
    fancy_message(request, "You successfully logged out", level="success")
    return redirect("account:login")
