from django.shortcuts import render


# Create your views here.


def home(request, *args, **kwargs):
    my_context = {
        "Title": "Home"
    }
    return render(request, "home.html", my_context)
