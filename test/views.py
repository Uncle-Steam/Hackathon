from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response (handler)

user = {
    'username': 'Tritop21',
    'type': 'Startup'
}

abouts = {
    'cocreators': ['Ananda', 'Averil', 'Janson', 'Weipin', 'Winsen']
}


def home(request):
    context = {
        'data': user
    }
    return render(request, "test.html", context)


def about(request):
    context = {
        'data': abouts
    }
    return render(request, "about.html", context)


def index(request):
    context = {
        'data': index,
        'title': "Login"
    }
    return render(request, "index.html", context)


def signup(request):
    context = {
        'title': "Sign Up"
    }
    return render(request, "signup.html", context)
